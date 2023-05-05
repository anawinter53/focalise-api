from unittest import mock
from flask import g
import pytest
from application.models import User
import json


def test_app_welcome(api):
    res = api.get('/')
    assert res.text == "Welcome to the API!"

def test_app_get_user(api):
    res = api.get('/users')
    assert res.status_code == 200 
    

def test_app_create_user(api, test_db, correct_user_data):
    user_model = User("users", test_db)
    with api.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = api.post('/users/new', json=correct_user_data)
        assert res.status_code == 201

def test_app_create_user_error(api, test_db, incorrect_user_data):
    user_model = User("users", test_db)
    with api.application.app_context():
        g.user_model = user_model

        res = api.post('/users/new', json=incorrect_user_data)
        assert res.status_code == 400



# body = { 
#     "username": "test1" 
#     "email": "test1@test.com"
#     "password: "test1"
#     }
# @pytest.mark.parametrize('payload, expected_status_code', [( body )], 201)

# def test_app_create_user(api):
#     res = api.post('/users/new')
#     assert res.status_code == 400
#     assert 'Missing parameters' in res.json['error']


#     @pytest.mark.parametrize(('payload', 'expected_status_code'), [(test0, 200), (test1, 400), (test2, 400), (test3, 400)])
# def test_response_code(payload, expected_status_code):
#     url = "https://xxxxx.com/category"

#     headers = {
#         'Content-Type': 'application/json',
#         'x-api-key': 'ju876djg3jd8'
#     }

#     response = requests.request("POST", url, headers=headers, json=payload)
#     assert response.status_code == expected_status_code
