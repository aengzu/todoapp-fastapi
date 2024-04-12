from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from typing import Annotated

from database import SessionLocal
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

def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
@router.post("/auth", status_code =status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
        create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        usedbrname=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        # 비밀 번호는 해싱되어야함.
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    db.add(create_user_model)
    db.commit()




# 인증. 라우터 패키지 안에 존재
@router.get("/auth")
async def get_user():
    return {'user': 'authenticated'}


