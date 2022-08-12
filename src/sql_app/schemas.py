import datetime
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    
class User(UserCreate):
    id: int

    class Config:
        orm_mode = True
