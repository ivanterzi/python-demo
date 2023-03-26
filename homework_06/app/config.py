import datetime
from string import ascii_lowercase
import secrets
import os


class Config(object):
    DEBUG = False
    TESTING = False
    ENV = ""
    SECRET_KEY = ''.join(secrets.choice(i)
                         for i in [x + ascii_lowercase[int(x)] for x in str(datetime.datetime.now()) if x.isdigit()])
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://username:passwd!@localhost:5432/blog")
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://username:passwd!@pg:5432/blog")


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True
    ENV = "testing"
    SQLALCHEMY_ECHO = True