import pytest
from application import routes

@pytest.fixture
def api():
    api = routes.app.test_client()
    return api
