from flask import Blueprint
from app.models import Category

bp = Blueprint('blog', __name__)

from app.blog import routes

@bp.app_context_processor
def inject_categories():
    categories = Category.query.all()
    return dict(categories=categories)