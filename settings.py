from os import environ

SQLALCHEMY_DATABASE_URI = environ.get('DB_URL')
SECRET_KEY = environ.get('SECRET_KEY')

