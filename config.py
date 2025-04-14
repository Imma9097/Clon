import os

class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/clon_point_credit'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debug mode
    DEBUG = True