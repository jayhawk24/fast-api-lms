from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    email: str
    is_acitve: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return user


@app.get("/users/{user_id}")
async def get_user(
    id: int = Path(..., description="The ID of the user to get", gt=0),
    q: str = Query(None, max_length=5),
):
    return {"user": [id], "query": q}
