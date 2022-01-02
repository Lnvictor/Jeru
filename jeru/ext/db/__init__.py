from os import getenv

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DB_URL")
    db.init_app(app)
