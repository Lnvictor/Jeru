from flask import Flask

from .ext import database


def create_app(**config):
    app = Flask(__name__)
    database.init_app(app)
    return app


def create_app_wsgi():
    app = create_app()
    return app
