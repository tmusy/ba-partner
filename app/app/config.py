# -*- coding: utf-8 -*-
import os

from .utils import make_dir


class BaseConfig(object):

    PROJECT = "ba-partner"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    INSTANCE_FOLDER_PATH = os.path.join(PROJECT_ROOT, 'instance')
    make_dir(INSTANCE_FOLDER_PATH)

    DEBUG = False
    TESTING = False

    ADMINS = ['tm@woosh.ch']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'a bad key'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    make_dir(LOG_FOLDER)

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    make_dir(UPLOAD_FOLDER)


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLITE for prototyping.
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BaseConfig.INSTANCE_FOLDER_PATH + '/db.sqlite'

    # DATABASE SETTINGS
    pg_db_username = 'postgres'
    pg_db_password = ''
    pg_db_name = 'ba'
    pg_db_hostname = 'postgres'

    # PostgreSQL
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=pg_db_username,
        DB_PASS=pg_db_password,
        DB_ADDR=pg_db_hostname,
        DB_NAME=pg_db_name)

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    #CACHE_TYPE = 'simple'
    #CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail: http://pythonhosted.org/flask-mail/
    # https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'thierry.musy@gmail.com'
    MAIL_PASSWORD = 'yourpass'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class TestConfig(BaseConfig):
    TESTING = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

    UPLOAD_FOLDER = os.path.join('/tmp', 'uploads')
    make_dir(UPLOAD_FOLDER)