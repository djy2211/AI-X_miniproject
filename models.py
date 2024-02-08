from email.policy import default
from sqlalchemy import Column, Integer, LargeBinary, String
from database import Base

class User(Base): # 사진 이름과 경로를 저장하기 위해서 모델 클래스 생성
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100)) # 사진 이름
    user_image = Column(String(1000)) # 이미지 경로
