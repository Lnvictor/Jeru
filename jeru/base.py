from flask import Flask

from .blueprints import init_app as init_app_bp
from .ext import db


def create_app(**config):
    app = Flask(__name__)
    db.init_app(app)
    return app


def create_app_wsgi():
    app = create_app()
    db.init_app(app)
    init_app_bp(app)
    return app
