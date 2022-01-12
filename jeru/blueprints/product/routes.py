import json
from sys import prefix

from flask import Blueprint, request
from flask.json import jsonify

from ...ext.http_auth import auth
from .controllers import create_product, search_product

bp = Blueprint("products", __name__, url_prefix="/product")


@bp.route("/", methods=["POST"])
@auth.login_required
def index():
    data = json.loads(request.data)
    create_product(data)
    return jsonify({"message": "Produto criado"}), 201


@bp.route("/search", methods=["POST"])
@auth.login_required
def search():
    data = json.loads(request.data)
    return jsonify(search_product(data))
