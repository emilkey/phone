import os
import logging

from flask import Blueprint, request, abort, url_for
from twilio.twiml.voice_response import Conference, Dial, Gather, VoiceResponse
from phone import validate_request

bp = Blueprint('conference', __name__, url_prefix='/conference')


@bp.route('/join', methods=['POST'])
def join():
    if os.environ.get('FLASK_ENV') != 'development':
        if not validate_request():
            logging.info('Request failed validation')
            return abort(400)
    pin_entered = request.form.get('Digits')
    response = VoiceResponse()
    dial = Dial()
    if pin_entered == os.environ.get('PHONE_CONF_LEADER_PIN'):
        dial.conference(
            os.environ.get('PHONE_CONF_ROOM_NUMBER'),
            start_conference_on_enter=True)
        response.append(dial)
    elif pin_entered == os.environ.get('PHONE_CONF_PARTICIPANT_PIN'):
        dial.conference(
            os.environ.get('PHONE_CONF_ROOM_NUMBER'),
            start_conference_on_enter=False)
        response.append(dial)
    else:
        response.say('Invalid pin entered.')
    return str(response)


@bp.route('/getpin')
def get_pin():
    response = VoiceResponse()
    gather = Gather(input='dtmf', timeout=10, num_digits=4)
    gather.say('Please enter your conference pin.')
    response.append(gather)
    response.redirect(url_for('conference.join'), method='GET')
    return str(response)
