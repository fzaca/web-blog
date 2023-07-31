from flask import Blueprint, session, redirect, url_for, g
from functools import wraps
from app.models import User

bp = Blueprint('auth', __name__)

from app.auth import routes

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.app_context_processor
def inject_user():
    return dict(user=g.user)