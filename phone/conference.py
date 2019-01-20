from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from twilio.twiml.voice_response import VoiceResponse

bp = Blueprint('conference', __name__, url_prefix='/conference')


@bp.route('/conference')
def join():
    pass
