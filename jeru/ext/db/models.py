from . import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(80), unique=True)
    email = db.Column("email", db.String(120), unique=True, nullable=False)
    birthday = db.Column("birthday", db.DateTime)
    password = db.Column("password", db.String(15))
    has_email_verified = db.Column("has_email_verified", db.Boolean)
    last_email_sended_at = db.Column("las_email_sended_at", db.DateTime)
    last_token_sended = db.Column("password", db.String(15))
