import json
from unittest import mock
from flask import g
from application.models import User

def test_get_sensory_data(client):
    res = client.get('/sensory/')
    assert res.status_code == 200 

    data = json.loads(res.data)
    assert len(data) == 15
    assert data[0]['sensory_id'] == 1
    assert data[0]['video_category'] == 'Music'
    assert data[0]['video_url'] == 'https://www.youtube.com/embed/zuCRSwWssVk'

def test_get_sensory_data_by_id(client):
    res = client.get('/sensory/id/2')
    assert res.status_code == 200 

    data = json.loads(res.data)
    assert len(data) == 3
    assert data['sensory_id'] == 2
    assert data['video_category'] == 'Music'
    assert data['video_url'] == 'https://www.youtube.com/embed/lE6RYpe9IT0'

def test_get_sensory_data_by_category(client):
    res = client.get('/sensory/animals')
    assert res.status_code == 200 

    # data = json.loads(res.data)
    # assert len(data) == 3
    # assert data[0]['sensory_id'] == 2
    # assert data[0]['video_category'] == 'Music'
    # assert data[0]['video_url'] == 'https://www.youtube.com/embed/lE6RYpe9IT0'
