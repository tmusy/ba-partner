# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migration = Migrate()

# from flask.ext.mail import Mail
# mail = Mail()
#
# from flask.ext.login import LoginManager
# login_manager = LoginManager()
#
# from flask.ext.security import Security
# security = Security()
#
# from flask.ext.admin import Admin
# admin = Admin()
#
# from flask.ext.restless import APIManager
# api = APIManager()