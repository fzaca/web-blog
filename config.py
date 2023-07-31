import os

from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # export DATABASE_URI="postgresql://username:password@host:port/database_name"
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
