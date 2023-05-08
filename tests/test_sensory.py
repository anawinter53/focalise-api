import json
from unittest import mock
from flask import g
from application.models import User

def test_get_messages(client):
    res = client.get('/sensory/')
    assert res.status_code == 200 

    data = json.loads(res.data)
    assert len(data) == 15
    assert data[0]['sensory_id'] == 1
    assert data[0]['video_category'] == 'Music'
    assert data[0]['video_url'] == 'https://www.youtube.com/watch?v=zuCRSwWssVk'
