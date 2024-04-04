from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# 기본적으로 SQLite 는 하나의 스레드만 통신을 허용한다.
# 다른 종류의 요청에 대해 같은 연결을 공유할 때 발생하는 문제 방지하고자 check_same_thread 사용
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}  # Corrected parameter
)
# 애플리케이션에서 사용할 세션로컬 : 엔진에 바인딩하고 자동 커밋 X, 자동 플러시 X
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 데이터베이스 오브젝트 만들기
Base = declarative_base()
