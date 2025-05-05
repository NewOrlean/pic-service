import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    CLOUDINARY_NAME = os.getenv("CLOUDINARY_NAME")
    CLOUDINARY_KEY = os.getenv("CLOUDINARY_KEY")
    CLOUDINARY_SECRET = os.getenv("CLOUDINARY_SECRET")