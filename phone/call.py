import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from twilio.twiml.voice_response import VoiceResponse

bp = Blueprint('call', __name__, url_prefix='/call')


@bp.route('/forward')
def forward():
    r = VoiceResponse()
    r.dial(os.environ['PHONE_FORWARD_NUMBER'])
    return str(r)
