from flask import request
from src.infra.drivers.jwt_handler import JwtHandler

def auth_jwt_verify():
    jwt_handle = JwtHandler()
    raw_token = request.headers.get("Authorization")

    if not raw_token:
        raise Exception("Invalid Auth informations")

    token = raw_token.split()[1]
    token_information = jwt_handle.decode_jwt_token(token)

    return token_information
    