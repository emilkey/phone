from flask import Blueprint

bp = Blueprint('conference', __name__, url_prefix='/conference')


@bp.route('/conference')
def join():
    pass
