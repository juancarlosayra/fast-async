from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from db import engine
from crud import CRUD
from schemas import UserModel, UserCreateModel
from typing import List
from models import User
import uuid
from http import HTTPStatus

app = FastAPI(
    title="Noted API",
    description="Simple note taking service",
    docs_url="/"
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

db = CRUD()

@app.get("/users", response_model=List[UserModel])
async def get_all_users():
    user = await db.get_all(session)
    return user

@app.get("/users/{user_id}")
async def get_by_id(note_id):
    user = await db.get_by_id(session, note_id)
    
    return user


@app.post("/users", status_code=HTTPStatus.CREATED)
async def create_user(user_data:UserCreateModel):
    new_user = User(
        id = user_data.user_id,
        user_name = user_data.user_name  
    )
    
    user = await db.add(session, new_user) 
    return user

@app.patch("/users/{users_id}")
async def update_user(user_id:int, data:UserCreateModel):
    user =  await db.update(session, user_id, data = {'user_name':data.user_name})
    
    return user

@app.delete("/users/{user_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_user(user_id):
    user = await db.get_by_id(session, user_id)
    result = await db.delete(session, user)
    
    return result