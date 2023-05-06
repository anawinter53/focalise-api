from flask import Flask
from flask_cors import CORS
import pytest
from application import routes
from application import app as flask_app
import requests
import json
import testing.postgresql
from sqlalchemy import create_engine
from application.models import User
from application.routes import *

@pytest.fixture()
def app():
    return flask_app

@pytest.fixture()
def client(app):
    with app.test_client() as test_client:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.register_blueprint(user_routes, name ='users', url_prefix="/users")
        app.register_blueprint(task_routes, name ='tasks', url_prefix="/tasks")
        app.register_blueprint(sensory_routes, name ='sensorys', url_prefix="/sensory")
        app.register_blueprint(setting_routes, name ='settings', url_prefix="/settings")
        app.register_blueprint(message_routes, name ='messages', url_prefix="/messages")
        yield test_client

# possible fix - recreate blueprint and assign to app
# @pytest.fixture()
# def setUp(self):
#     super(client, self).setUp()
#     app.config['TESTING'] = True
#     app.config['DEBUG'] = False
#     self.assertEquals(app.debug, False)

#     app = Flask(__name__)
#     CORS(app)

#     app.register_blueprint(user_routes, url_prefix="/users")
#     app.register_blueprint(task_routes, url_prefix="/tasks")
#     app.register_blueprint(sensory_routes, url_prefix="/sensory")
#     app.register_blueprint(setting_routes, url_prefix="/settings")
#     app.register_blueprint(message_routes, url_prefix="/messages")



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
def created_user(user_model, correct_user_data):
    return user_model.register(correct_user_data)

# Tests for user model
def test_create_user(user_model, correct_user_data):
    inserted_id = user_model.register(correct_user_data)
    assert inserted_id is not None


# create a test db connection
# @pytest.fixture
# def test_db():
#     return get_connection("TEST_DB_URL")

# import requests
# import json

# url = 'https://somedomain.com'
# body = {'name': 'Maryja'}
# headers = {'content-type': 'application/json'}

# r = requests.post(url, data=json.dumps(body), headers=headers)

# def new_user(monkeypatch):
#     url = '/'
#     user = [{'username': 'test1', 'email': 'test1@test.com', 'password': 'test1'}]
#     monkeypatch.setattr(routes, "user", user)
#     client = routes.app.test_client()
#     return client
