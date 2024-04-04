from fastapi import APIRouter
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

#pydantic
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name : str
    password: str
    role: str

@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        # 비밀 번호는 해싱되어야함.
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    return create_user_model


# 인증. 라우터 패키지 안에 존재
@router.get("/auth")
async def get_user():
    return {'user': 'authenticated'}


