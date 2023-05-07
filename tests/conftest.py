import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pytest
from application import app as flask_app
import testing.postgresql
from sqlalchemy import create_engine
from application.models import User
from application.routes import *

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("TEST_DB_URL")
# db = SQLAlchemy(app)
# db.init_app(app)

@pytest.fixture()
def app():
    # app.config['TESTING'] = True
    return flask_app

@pytest.fixture()
def client(app):
    with app.test_client() as test_client: 
        yield test_client

@pytest.fixture()
def test_db():
    with testing.postgresql.Postgresql() as postgresql:
        engine = create_engine(postgresql.url())

        import psycopg2
        db = psycopg2.connect(**postgresql.dsn())

@pytest.fixture
def user_model(test_db):
    return User("users", test_db)

@pytest.fixture
def correct_user_data():
    return {
        'username': 'test2',
        'email': 'test2@test.com',
        'password': 'testing'
    }

@pytest.fixture
def incorrect_user_data():
    return {
        'username': '',
        'email': 34,
        'password': 'testing'
    }

@pytest.fixture
def correct_login_data():
    return {
        'username': 'test2',
        'password': 'testing'
    }

@pytest.fixture
def incorrect_login_data():
    return {
        'username': 'test2',
        'password': 'oops'
    }

@pytest.fixture
def correct_task_data():
    return {
        "category_name": "Python",
        "task_desc": "Find some python tests",
        "task_name": "More Python",
        "task_url": "",
        "user_id": 1
    }
