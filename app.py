""" from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")  # /items/5?q=Hellolesploucs
def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# /items2/iphone14?needy=youNeedThis {"item_id":"iphone14","needy":"youNeedThis","skip":0,"limit":null}
@app.get("/items2/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/feur")
def read_feur():
    return {"Message": "Feur", "Quoi?": "Feur lol"}
 """