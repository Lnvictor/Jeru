import json

from flask import Blueprint, jsonify, request

from .controllers import create_user, get_all_users

bp = Blueprint("auth", __name__, url_prefix="auth")


@bp.route("/user", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(get_all_users()), 200
    data = json.loads(request.data)
    return jsonify(create_user(data)), 201
