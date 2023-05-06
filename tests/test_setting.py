from unittest import mock
from flask import g
from application.models import User

def test_get_setting(client):
    res = client.get('/settings/1')
    assert res.status_code == 200 


