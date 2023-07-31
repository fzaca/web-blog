from flask import Flask, g
from flask_migrate import Migrate

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.models import User, Post, Comment, Category

    # Register blueprints here
    from app.main import bp as main_bp
    from app.auth import bp as auth_bp
    from app.blog import bp as blog_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    @app.route('/test')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
