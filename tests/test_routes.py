def test_app_welcome(api):
    res = api.get('/')
    assert res.text == "Welcome to the API!"

def test_app_get_user(api):
    res = api.get('/users')
    assert res.status_code == 200 

def test_app_create_user(api):
    res = api.post('/users/new')
    assert res.status_code == 400
    assert 'Missing parameters' in res.json['error']
