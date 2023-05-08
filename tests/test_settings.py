from unittest import mock
from flask import g
from application.models import UserSetting

def test_get_setting(client):
    res = client.get('/settings/1')
    assert res.status_code == 200 

def test_update_setting(client, test_db, update_settings_data):
    user_model = UserSetting("users", test_db)
    with client.application.app_context():
        g.user_model = user_model

        mock_get = mock.Mock()
        mock_get.return_value = '70'
        g.user_model.create = mock_get

        res = client.put('/settings/1', json=update_settings_data)
        assert res.status_code == 200
