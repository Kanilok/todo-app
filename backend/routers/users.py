import jwt
from .models import User_Pydantic, UserIn_Pydantic, Users
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from datetime import datetime, timedelta


router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)

JWT_SECRET = "idkwhatisasecret"
ALGORITHM = "HS256"
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

def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.password, form_data.username)


    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "invalid username or password"
        )
    
    user_obj = await User_Pydantic.from_tortoise_orm(user)

    access_token_expires = timedelta(minutes=15)
    access_token = create_jwt_token(
        data={"sub": user_obj.dict()["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = await Users.get(username = payload.get("sub"))
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "invalid username or password"
        )

    return await User_Pydantic.from_tortoise_orm(user)
        

@router.get("/me", response_model = User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user 
