"""__init__.py."""
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(environment='Development'):
    """create_app method."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.{}'.format(environment.capitalize()))
    app.config.from_pyfile('config.py')

    from .views import app as _app
    app.register_blueprint(_app)

    db.init_app(app)

    return app
