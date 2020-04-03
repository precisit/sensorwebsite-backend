import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Precisit123@bankvader-db.ct21dnnypyko.eu-north-1.rds.amazonaws.com:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False