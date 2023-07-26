import jwt
from .models import User_Pydantic, UserIn_Pydantic, Users
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt

router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)

JWT_SECRET = "idkwhatisasecret"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "users/login")

class User(BaseModel):
    username: str
    hashed_password: str


@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    try:
        await Users.get(username = user.username)
    except:
        user_obj = Users(username = user.username, hashed_password = bcrypt.hash(user.hashed_password))
        await user_obj.save()
        return await User_Pydantic.from_tortoise_orm(user_obj)
    else:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "username already taken"
        )


async def authenticate_user(password: str, username: str):
    try:
        user = await Users.get(username = username)
    except:
        return False
    else:
        if not user.verify_password(password):
            return False
        else:
            return user


@router.post("/login")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.password, form_data.username)

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "invalid username or password"
        )

    user_obj = await User_Pydantic.from_tortoise_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return {"access_token" : token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = await Users.get(id = payload.get("id"))
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "invalid username or password"
        )

    return await User_Pydantic.from_tortoise_orm(user)
        

@router.get("/me", response_model = User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user 
