"""
TODO:
    Implementar a funcionalidade de Busca
"""

import json

from flask import Blueprint, request
from flask.json import jsonify

from ..auth.http_auth import auth
from .controllers import create_product

bp = Blueprint("products", __name__)


@bp.route("/product", methods=["POST"])
@auth.login_required
def index():
    data = json.loads(request.data)
    create_product(data)
    return jsonify({"message": "Produto criado"}), 201
