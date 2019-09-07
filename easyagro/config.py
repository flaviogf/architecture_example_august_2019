from dotenv import load_dotenv

from os import environ

load_dotenv('.env')


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production:
    pass


class Testing:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
