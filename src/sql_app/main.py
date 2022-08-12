from typing import List
import datetime
import uvicorn
import streamlit as st
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

import crud, models, schemas
# from .database import SessionLocal, engine
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === routing === #
# Raed
@app.get("/app/users", response_model = List[schemas.Users])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# Create
@app.post("/app/users", response_model=schemas.Users)
async def create_user(actress: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


    
if __name__ == "__main__":
    # uvicorn.run("main.app")
    uvicorn.run(app.app,host="0.0.0.0", port=8080)
