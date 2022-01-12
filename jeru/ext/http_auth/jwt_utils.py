import os

import jwt
from cryptography.hazmat.primitives import serialization
from decouple import config

files_path = os.getcwd()

pwd = config("TOKEN_PASSWORD").encode()
private_key = open(files_path + "/.ssh/id_rsa", "r").read()
public_key = open(files_path + "/.ssh/id_rsa.pub", "r").read()
key = serialization.load_ssh_private_key(private_key.encode(), pwd)
p_key = serialization.load_ssh_public_key(public_key.encode(), pwd)


def generate_jwt_token(user):
    payload = {"user_id": user.id, "user_name": user.username}

    return jwt.encode(payload=payload, key=key, algorithm="RS256")


def validate_token(token):
    try:
        data = jwt.decode(
            jwt=token,
            key=p_key,
            algorithms=[
                "RS256",
            ],
        )
        return True
    except:
        return False
