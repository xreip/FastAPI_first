from fastapi import FastAPI, Depends
from config.config import initiate_database

from enum import Enum

# from app.api.api import api_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def list_users():
    return {"message": "list user route"}

# Before by id !


@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return {"user_id": user_id}


@app.post("/")
async def post():
    return {"message": "hello from post"}


@app.put("/")
async def put():
    return {"message": "hello from PUT"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"Your food": food_name, "message": "You're healthy"}

    if food_name.value == "fruits":
        return {"Your food": food_name, "message": "You like fruits"}

    return {"Your food": food_name, "message": "You like things..."}

# app.include_router(api_router) # ADD THE CENTRAL ROUTER


@app.on_event("startup")
async def app_init():
    await initiate_database()
