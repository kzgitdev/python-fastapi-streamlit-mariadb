from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
import models, schemas

# get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.User).offset(skip).limit(limit).all()

# regist user
def create_user(db: Session, user: schemas.User):
  db_actress = models.User(name=user.name)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user
