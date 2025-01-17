from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
DATABASE_NAME = os.getenv('DATABASE_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
GOOGLE_CLOUD_CREDENTIALS_PATH = os.getenv('GOOGLE_CLOUD_CREDENTIALS_PATH')
GOOGLE_CLOUD_BUCKET_NAME = os.getenv('GOOGLE_CLOUD_BUCKET_NAME')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

class Settings(BaseSettings):
    GOOGLE_CLOUD_CREDENTIALS_PATH: str = GOOGLE_CLOUD_CREDENTIALS_PATH
    GOOGLE_CLOUD_BUCKET_NAME: str = GOOGLE_CLOUD_BUCKET_NAME
    GEMINI_API_KEY: str = GEMINI_API_KEY
    MONGO_URL: str = MONGO_URL
    DATABASE_NAME: str = DATABASE_NAME
    SECRET_KEY: str = SECRET_KEY
    ALGORITHM: str = ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(ACCESS_TOKEN_EXPIRE_MINUTES)
    class Config:
        env_file = '.env'

settings = Settings() 