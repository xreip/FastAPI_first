import jwt
from os import getenv
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = getenv("JWT_SECRET")
