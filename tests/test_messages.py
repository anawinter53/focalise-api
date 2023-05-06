from unittest import mock
from flask import g
from application.models import User

def test_get_messages(client):
    res = client.get('/messages/')
    assert res.status_code == 200 
