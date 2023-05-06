from unittest import mock
from flask import g
from application.models import User
import json

def test_app_get_user(client):
    res = client.get('/users/')
    assert res.status_code == 200 

def test_show_users(client):
    res = client.get('/users/1')
    assert res.status_code == 200

def test_app_create_user(client, test_db, correct_user_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.post('/users/register', json=correct_user_data)
        assert res.status_code == 201

def test_app_create_user_error(client, test_db, incorrect_user_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        res = client.post('/users/register', json=incorrect_user_data)
        assert res.status_code == 400

