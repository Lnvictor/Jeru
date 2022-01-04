from ...models import User
from ..db import db


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


def populate_db():
    data = [
        User(),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return User.query.all()
