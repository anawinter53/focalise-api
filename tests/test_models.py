import pytest
from application.models import User
from flask import g
import json

def test_create_user(test_db, correct_user_data):
    user_model = User("users", test_db)

    inserted_id = user_model.create_user_route(correct_user_data)
    users = json.loads(inserted_id)
    assert any(i['username'] == 'test2' for i in users['users'])



# def test_get_user(test_db, correct_user_data):
#     user_model = User("users", test_db)

#     inserted_id = user_model.create(correct_user_data)
#     user = user_model.get(str(inserted_id))
#     assert user is not None
#     assert user["_id"] == inserted_id
