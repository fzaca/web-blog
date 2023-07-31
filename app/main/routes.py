from flask import render_template, redirect, url_for
from app.main import bp
from app.auth import login_required

@bp.route('/')
def index():
    return redirect(url_for('auth.login'))

