from datetime import datetime

from jeru.ext.db import db
from jeru.models import User


def create_user(data):
    """
    TODO:
        Implement the password in a encripted form using bcrypt
    """
    date = [int(n) for n in data["birthday"].split("/")]
    data["birthday"] = datetime(day=date[0], month=date[1], year=date[2])

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user


def get_all_users():
    return User.query.order_by(User.email).all()


def get_user_by_id(id):
    return User.query.filter_by(id=id).first()


def update_user(id, data):
    user = get_user_by_id(id)

    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()
    return user


def delete_user(id):
    try:
        user = get_user_by_id(id)
        db.session.delete(user)
        db.session.commit()
        return True
    except:
        return False
