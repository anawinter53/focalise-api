from unittest import mock
from flask import g
from application.models.models import User

def test_get_user(client):
    res = client.get('/users/')
    assert res.status_code == 200 

def test_show_users(client):
    res = client.get('/users/1')
    assert res.status_code == 200

def test_create_user(client, test_db, correct_user_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.post('/users/register', json=correct_user_data)
        assert res.status_code == 201

def test_create_user_error(client, test_db, incorrect_user_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        res = client.post('/users/register', json=incorrect_user_data)
        assert res.status_code == 400

def test_login(client, test_db, correct_login_data):
    user_model = User("users", test_db)
    g.user_model = user_model

    res = client.post('/users/login', json=correct_login_data)
    assert res.status_code == 200

def test_login_error(client, test_db, incorrect_login_data):
    user_model = User("users", test_db)
    g.user_model = user_model

    res = client.post('/users/login', json=incorrect_login_data)
    assert res.status_code == 403

# def test_logout(client, test_db, correct_login_data):
#     user_model = User("users", test_db)
#     g.user_model = user_model
    
#     res = client.post('/users/logout', json=correct_login_data)
#     assert res.status_code == 200
