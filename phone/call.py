import os

from flask import Blueprint
from twilio.twiml.voice_response import VoiceResponse

bp = Blueprint('call', __name__, url_prefix='/call')


@bp.route('/forward')
def forward():
    resp = VoiceResponse()
    resp.dial(os.environ['PHONE_FORWARD_NUMBER'])
    return str(resp)
