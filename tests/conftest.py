import pytest
from application import routes
import requests
import json

@pytest.fixture
def api():
    api = routes.app.test_client()
    return api


# import requests
# import json

# url = 'https://somedomain.com'
# body = {'name': 'Maryja'}
# headers = {'content-type': 'application/json'}

# r = requests.post(url, data=json.dumps(body), headers=headers)

def new_user(monkeypatch):
    url = '/'
    user = [{'username': 'test1', 'email': 'test1@test.com', 'password': 'test1'}]
    monkeypatch.setattr(routes, "user", user)
    client = routes.app.test_client()
    return client
