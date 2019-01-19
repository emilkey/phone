import os


def test_forward(client):
    response = client.get('/call/forward')  # <class 'flask.wrappers.Response'>
    assert '<Dial>{}</Dial>'.format(os.environ['PHONE_FORWARD_NUMBER']) in response.data.decode()
    assert response.status_code == 200
