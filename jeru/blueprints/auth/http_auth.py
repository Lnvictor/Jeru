from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme="Bearer")


tokens = ["tokena", "tokenb"]


@auth.verify_token
def verify_token(token):
    return True if token in tokens else None
