import os
from unittest import mock


def test_forward(client):
    json_data = {}
    response = client.post('/call/forward', json=json_data)  # <class 'flask.wrappers.Response'>
    assert '<Dial>{}</Dial>'.format(os.environ['PHONE_FORWARD_NUMBER']) in response.data.decode()
    assert response.status_code == 200


def test_validate(client):
    with mock.patch.dict('os.environ', {'FLASK_ENV': 'production'}):
        json_data = {}
        response = client.post('/call/forward', json=json_data)  # <class 'flask.wrappers.Response'>
        assert response.status_code == 400
