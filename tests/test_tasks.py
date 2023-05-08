from unittest import mock
from flask import g
from application.models.models import User

def test_get_tasks_by_user(client):
    res = client.get('/tasks/1')
    assert res.status_code == 200 

def test_get_tasks_by_category(client):
    res = client.get('/tasks/1/Python')
    assert res.status_code == 200 

def test_create_task(client, test_db, correct_task_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.post('/tasks/user/1', json=correct_task_data)
        assert res.status_code == 201
