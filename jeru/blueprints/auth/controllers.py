from datetime import datetime

import bcrypt

from jeru.ext.db import db
from jeru.models import User

from ...ext.http_auth import auth, jwt_utils


def create_user(data):
    date = [int(n) for n in data["birthday"].split("/")]
    data["birthday"] = datetime(day=date[0], month=date[1], year=date[2])
    data["password"] = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
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


def make_login(username, password):
    user = User.query.filter_by(username=username).first()
    if bcrypt.checkpw(password.encode(), user.password):
        return {"token": jwt_utils.generate_jwt_token(user), "status": 200}
    return {"message": "Invalid credentials", "status": 401}
