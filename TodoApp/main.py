from fastapi import FastAPI, Depends, HTTPException, Path
import models
from database import engine
from routers import auth, todos

app = FastAPI()  # FastAPI 애플리케이션 인스턴스 생성

# todos.db 가 없을 때만 아래 문장 실행되어야함.
# 이는 애플리케이션 시작 시 데이터베이스 스키마를 초기화하는 데 사용됩니다.
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
