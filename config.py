"""Flask configuration"""

from datetime import timedelta
from os import environ
from os import urandom
import os.path

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))
ACCESS_EXPIRES = timedelta(hours=1)


class Config:
    """Flask base config"""
    SECRET_KEY = environ.get("SECRET_KEY") or urandom(24)
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Subdomain testing
    SERVER_NAME = "neurothrone.tld:5000"

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(basedir, 'app/data.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    # app.config["JWT_SECRET_KEY"] = os.urandom(24)  # if necessary to differ from app.secret_key
    # JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES

    # Mail
    # MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    # MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # ADMINS = ["zane.kortex@gmail.com"]
    # ADMINS = ["your-email@example.com"]

    # Posts
    # POSTS_PER_PAGE = 3

    # Babel
    # LANGUAGES = ["en", "sv_SE"]

    # Microsoft Translator API
    # MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get("DEVELOPMENT_DATABASE_URI")


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get("PRODUCTION_DATABASE_URI")


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
