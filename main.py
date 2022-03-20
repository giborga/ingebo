# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# endpoint /users
@app.get("/users")
async def read_users():
    return {"users": ['user1', 'user2', 'user3', 'user4', 'user5']}


@app.get("/users/{id}")
async def read_user(id: int):
    return {"user": "User 1"}


class User(BaseModel):
    name: str


@app.post("/users")
async def create_user(user: User):
    return {"status": 'User {} created'.format(user.name)}


@app.put("/users/{id}")
async def update_user(id: int, user: User):
    return {"status": 'User with id {}, {} was updated'.format(id, user.name)}


@app.delete("/users/{id}")
async def delete_user(id: int):
    return {"status": 'User {} deleted'.format(id)}