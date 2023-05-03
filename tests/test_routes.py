

def test_app_get_user(api):
    res = api.get('/users')
    assert res.status_code == 200 
