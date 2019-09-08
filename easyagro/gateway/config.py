from dotenv import load_dotenv

from os import environ

load_dotenv('.env')


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    pass


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
