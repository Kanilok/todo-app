import jwt
from .models import User_Pydantic, UserIn_Pydantic, Users
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from password_strength import PasswordPolicy
from datetime import datetime, timedelta
from typing import List

policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,  
    special=1 
)

router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)

JWT_SECRET = "idkwhatisasecret"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "users/login")


@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    try:
        await Users.get(username = user.username)
    except:
        if(policy.test(user.hashed_password) == []):
            user_obj = Users(username = user.username, hashed_password = bcrypt.hash(user.hashed_password))
            await user_obj.save()
            return await User_Pydantic.from_tortoise_orm(user_obj)
        else:
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                detail = "password is too weak"
            )
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

    access_token_expires = timedelta(minutes=60)
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
    

@router.post("/admin", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic, user_admin: User_Pydantic = Depends(get_current_user)):
    if user_admin.admin:
        try:
            await Users.get(username = user.username)
        except:
            if(policy.test(user.hashed_password) == []):
                user_obj = Users(username = user.username, hashed_password = bcrypt.hash(user.hashed_password), verified = True, admin = True)
                await user_obj.save()
                return await User_Pydantic.from_tortoise_orm(user_obj)
            else:
                raise HTTPException(
                    status_code = status.HTTP_406_NOT_ACCEPTABLE,
                    detail = "password is too weak"
                )
        else:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = "username already taken"
            )
    else:
        raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "you must be an admin to create an admin"
            )


@router.get("/current", response_model = User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user


@router.get("/", response_model=List[User_Pydantic])
async def get_users(user: User_Pydantic = Depends(get_current_user)):
    if user.admin:
        return await User_Pydantic.from_queryset(Users.filter(admin = False))
    else:
        raise HTTPException(
                        status_code = status.HTTP_401_UNAUTHORIZED,
                        detail = "you must be an admin to see users"
                    )

@router.put("/{user_id}", response_model = User_Pydantic)
async def verify_user(user_id: int, user_admin: User_Pydantic = Depends(get_current_user)):
    if user_admin.admin:
        user_obj = await User_Pydantic.from_queryset_single(Users.get(id=user_id))
        await Users.filter(id=user_id).update(verified = not user_obj.dict()["verified"])
        return await User_Pydantic.from_queryset_single(Users.get(id=user_id))
    else:
        raise HTTPException(
                        status_code = status.HTTP_401_UNAUTHORIZED,
                        detail = "you must be an admin to verify users"
                    )