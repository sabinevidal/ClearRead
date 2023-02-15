import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    TESTING = environ.get("TESTING")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Image Upload Config
    UPLOAD_PATH = "main/static/images/"
    UPLOAD_EXTENSIONS = [".jpeg", ".jpg", ".png", ".gif", ".JPG"]
    MAX_CONTENT_LENGTH = 1024 * 1024 # 1MB

    # Database
    DATABASE_NAME = environ.get("DATABASE_NAME")
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI") or \
        'sqlite:///' + os.path.join(basedir, DATABASE_NAME)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Auth0
    AUTH0_CLIENT_ID = environ.get("AUTH0_CLIENT_ID")
    AUTH0_DOMAIN = environ.get("AUTH0_DOMAIN")
    AUTH0_CLIENT_SECRET = environ.get("AUTH0_CLIENT_SECRET")
    AUTH0_CALLBACK_URL = environ.get("AUTH0_CALLBACK_URL")
    AUTH0_AUDIENCE = environ.get("AUTH0_AUDIENCE")

    """Flask configuration."""

    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True