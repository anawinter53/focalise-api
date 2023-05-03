import pytest
from application import routes
import requests
import json
import testing.postgresql
from sqlalchemy import create_engine

# set up app
@pytest.fixture
def api():
    api = routes.app.test_client()
    return api

# create a test client
# @pytest.fixture
# def client(api):
#     with api.test_client() as test_client:
#         yield test_client

@pytest.fixture
def test_db():
    with testing.postgresql.Postgresql() as postgresql:
        engine = create_engine(postgresql.url())

        import psycopg2
        db = psycopg2.connect(**postgresql.dsn())

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
