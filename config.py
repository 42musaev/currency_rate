import os
from dotenv import load_dotenv

load_dotenv()


class Configuration(object):
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    PG_HOST = os.getenv('PG_HOST')
    DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}/{POSTGRES_DB}"
    DEBUG = os.getenv('DEBUG')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DB_URL
    SECRET_KEY = os.getenv('SECRET_KEY')
