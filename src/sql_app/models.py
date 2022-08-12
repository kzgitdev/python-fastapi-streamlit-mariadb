from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship

# データベースの中のテーブルを定義していく
class Actress(Base):
    __tablename__ = "actress"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
