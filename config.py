import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///calibration.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False