import pytest
from application.models import User
from flask import g
import json

def test_create_user(test_db, correct_user_data):
    user_model = User("users", test_db)

    inserted_id = user_model.create(correct_user_data)
    users = json.loads(inserted_id)
    assert any(i['username'] == 'test2' for i in users['users'])
