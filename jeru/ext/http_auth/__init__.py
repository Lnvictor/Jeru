from flask_httpauth import HTTPTokenAuth

from .jwt_utils import validate_token

auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    return validate_token(token)
