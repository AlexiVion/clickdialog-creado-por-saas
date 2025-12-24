import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.SECRET_KEY = os.getenv("SECRET_KEY", "dev")
        self.SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dev.db")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.JWT_SECRET = os.getenv("JWT_SECRET", "dev-jwt")
        self.MODULES_ENABLED = ["auth", "landingpages", "chatbot", "analytics", "integration"]
        self.MULTI_TENANT = True
