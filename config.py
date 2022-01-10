import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration class. Contains default configuration settings.
    """
    # Default settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', default='development')
    RESULT_BACKEND = os.getenv('RESULT_BACKEND')


class DevelopmentConfig(Config):
    DEBUG = True
