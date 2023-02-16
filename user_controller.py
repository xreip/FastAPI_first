""" import jwt
from os import getenv
from dotenv import load_dotenv
import datetime

load_dotenv()


def generate_access_token(id):
    JWT_SECRET = getenv("JWT_SECRET")
    access_lifetime = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
    payload = {'id': id, 'exp': access_lifetime}
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def decode_access_token(token):
    try:
        JWT_SECRET = getenv("JWT_SECRET")
        decoded = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        print(decoded)
        return "superbe token"
    except jwt.ExpiredSignatureError:
        return "mauvais token sadge, expired"
    except jwt.InvalidTokenError:
        return "mauvais token sadge"
 """
