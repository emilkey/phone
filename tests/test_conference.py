import os
from unittest import mock


def test_join_leader(client):
    pin = dict(Digits=os.environ.get('PHONE_CONF_LEADER_PIN'))
    response = client.post('/conference/join', data=pin)  # <class 'flask.wrappers.Response'>
    assert 'startConferenceOnEnter="true"' in response.data.decode()
    assert response.status_code == 200


def test_join_participant(client):
    pin = dict(Digits=os.environ.get('PHONE_CONF_PARTICIPANT_PIN'))
    response = client.post('/conference/join', data=pin)  # <class 'flask.wrappers.Response'>
    assert 'startConferenceOnEnter="true"' not in response.data.decode()
    assert '<Conference>' not in response.data.decode()
    assert response.status_code == 200


def test_join_invalid(client):
    pin = dict(Digits=1)
    response = client.post('/conference/join', data=pin)  # <class 'flask.wrappers.Response'>
    assert 'Invalid' in response.data.decode()
    assert response.status_code == 200
