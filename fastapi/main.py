import uuid
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from database import database, users

app = FastAPI()


class User(BaseModel):
    email: str
    name: str

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.post('/')
async def create_user(user: User):
    query = users.insert().values(
        name=user.name,
        email=user.email,
        id=uuid.uuid4(),
        created=datetime.utcnow(),
    )
    await database.execute(query)
    return user.dict()
