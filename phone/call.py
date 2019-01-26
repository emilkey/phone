import os
import logging

from flask import Blueprint, request, abort
from twilio.twiml.voice_response import VoiceResponse
from phone import validate_request

bp = Blueprint('call', __name__, url_prefix='/call')


@bp.route('/forward', methods=['POST'])
def forward():
    if os.environ.get('FLASK_ENV') != 'development':
        if not validate_request():
            logging.info('Request failed validation')
            return abort(400)
    resp = VoiceResponse()
    resp.dial(os.environ['PHONE_FORWARD_NUMBER'])
    return str(resp)
