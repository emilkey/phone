import os
import logging

from flask import Blueprint, request, abort
from twilio.twiml.voice_response import VoiceResponse
from twilio.request_validator import RequestValidator

bp = Blueprint('call', __name__, url_prefix='/call')


def validate_request() -> bool:
    validator = RequestValidator(os.environ['TWILIO_AUTH_TOKEN'])
    twilio_signature = request.headers.get('X-TWILIO-SIGNATURE', '')
    return validator.validate(request.url, request.form, twilio_signature)


@bp.route('/forward', methods=['POST'])
def forward():
    if os.environ.get('FLASK_ENV') != 'development':
        if not validate_request():
            logging.info('Request failed validation')
            return abort(400)
    resp = VoiceResponse()
    resp.dial(os.environ['PHONE_FORWARD_NUMBER'])
    return str(resp)
