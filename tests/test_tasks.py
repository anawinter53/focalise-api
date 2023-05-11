import json
from unittest import mock
from flask import g
from application.models import User

def test_get_tasks_by_user(client):
    res = client.get('/tasks/user/1')
    assert res.status_code == 200 

    data = json.loads(res.data)
    assert len(data) == 3
    assert data[0]['user_id'] == 1
    assert data[0]['task_id'] == 1
    assert data[0]['category_name'] == 'Python'
    assert data[0]['task_name'] == 'Python testing'
    assert data[0]['task_desc'] == 'Try and understand the concept of unit testing with Python'
    assert data[0]['task_url'] == 'https://realpython.com/python-testing/'

def test_get_tasks_by_category(client):
    res = client.get('/tasks/user/1/Python')
    assert res.status_code == 200 

    data = json.loads(res.data)
    assert len(data) == 1

def test_show_task_by_taskid(client):
    res = client.get('/tasks/2')
    assert res.status_code == 200

    data = json.loads(res.data)
    assert len(data) == 8
    assert data['user_id'] == 1
    assert data['task_id'] == 2
    assert data['category_name'] == 'Django'
    assert data['task_name'] == 'Django intro'
    assert data['task_desc'] == 'Start on Django'
    assert data['task_url'] == 'https://www.w3schools.com/django/django_intro.php'

def test_show_categories_by_userid(client):
    res = client.get('/tasks/user/1/categories')
    assert res.status_code == 200

    data = json.loads(res.data)
    assert len(data) == 3
    assert data[0] == "Python"
    assert data[1] == "Django"
    assert data[2] == "Design"

def test_create_task(client, test_db, correct_task_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.post('/tasks/user/1', json=correct_task_data)
        assert res.status_code == 201

def test_create_task_error(client, test_db, incorrect_task_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.post('/tasks/user/1', json=incorrect_task_data)
        assert res.status_code == 400

def test_update_task(client, test_db, correct_update_task_data):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.put('/tasks/1', json=correct_update_task_data)
        assert res.status_code == 200

def test_delete_task(client, test_db):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.delete('/tasks/4')
        assert res.status_code == 200

def test_delete_task_by_category(client, test_db):
    user_model = User("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.delete('/tasks/user/1/Design')
        assert res.status_code == 200
