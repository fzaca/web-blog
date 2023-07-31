from flask import Blueprint, g

bp = Blueprint('main', __name__)

from app.main import routes, errors