from enum import Enum

from fastapi import FastAPI, Depends, Query, Path
from pydantic import BaseModel

from config.config import initiate_database

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


# Query Params
fake_items_db = [
    {"item_name": "FOO"},
    {"item_name": "BAR"},
    {"item_name": "FOBAR"},
    {"item_name": "BARFOO"},
    {"item_name": "BFAO"},
]


# @app.get("/items")  # /items?skip=2 | /items?limit=1 | /items?skip=1&limit=3
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Lorem ipsum dolor sit."})
#     return item


""" 4. Request body """


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


""" 5. Query param & string validation """


@app.get("/items")
async def read_items(
    q: str
    | None = Query(
        None,
        min_lenght=3,
        max_length=10,
        title="Sample query string",
        description="This is a description",
        alias="item-query",
    ),
    required: str = Query(..., min_length=5),
    q_array: list[str] = Query(["foo", "bar"]),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/hidden")
async def hidden_query(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "Not found"}


# app.include_router(api_router) # ADD THE CENTRAL ROUTER
# @app.on_event("startup")
# async def app_init():
#     await initiate_database()

""" 6. Path parameters and numeric validation """


@app.get("/item_validation/{item_id}")
async def read_items_validation(
    item_id: int = Path(..., title="The id of the item to get", gt=10, le=100),
    q: str | None = Query(None, alias="item_query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
