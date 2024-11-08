import os

USERNAME = 'admin'
PASSWORD = 'password'
SECRET_KEY = 'secret-key'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URL = f'sqlite:///{os.path.join(BASE_DIR, "app.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
