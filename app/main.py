from fastapi import FastAPI, Depends
from config.config import initiate_database



# from app.api.api import api_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(api_router) # ADD THE CENTRAL ROUTER


@app.on_event("startup")
async def app_init():
    await initiate_database()
