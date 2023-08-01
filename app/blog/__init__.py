from flask import Blueprint
from app.models import Category
from app.extensions import db

bp = Blueprint('blog', __name__)

from app.blog import routes

@bp.app_context_processor
def inject_categories():
    categories = Category.query.all()
    return dict(categories=categories)

def create_categories():
    if not Category.query.first():
        categories = [
            'World',
            'Technology',
            'Design',
            'Culture',
            'Business',
            'Politics',
            'Opinion',
            'Science',
            'Health',
            'Style',
            'Travel',
            'Fitness',
        ]

        for category_name in categories:
            category = Category(name=category_name)
            db.session.add(category)

        db.session.commit()

create_categories()