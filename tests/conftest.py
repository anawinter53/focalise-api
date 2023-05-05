import pytest
from application import routes
import requests
import json
import testing.postgresql
from sqlalchemy import create_engine
from application.models import User

@pytest.fixture
def api():
    api = routes.app.test_client()
    return api

@pytest.fixture
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
