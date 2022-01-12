import json

from flask import Blueprint, jsonify, request

from ...ext.http_auth import auth, jwt_utils
from .controllers import (create_user, delete_user, get_all_users,
                          get_user_by_id, make_login, update_user)

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["POST"])
def login():
    data = json.loads(request.data)
    resp = make_login(data["username"], data["password"])
    return jsonify(resp), resp["status"]


@bp.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return jsonify({"users": [user.to_dict() for user in get_all_users()]}), 200
    data = json.loads(request.data)
    create_user(data)
    return jsonify({"message": "User created"}), 201


@bp.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def user_by_id(id):
    if request.method == "GET":
        return jsonify(get_user_by_id(id).to_dict()), 200
    elif request.method == "PUT":
        data = json.loads(request.data)
        return jsonify(update_user(id, data).to_dict()), 200

    delete_user(id)
    return jsonify({"message": "User deleted"}), 200
