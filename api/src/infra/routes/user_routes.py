from flask import Blueprint, jsonify, request
from src.infra.views.http_types.http_request import HttpRequest
from src.infra.composer.create_user_composer import create_user_composer
from src.infra.composer.authenticate_user_composer import authenticate_user_composer
from src.infra.errors.error_handle import handle_errors
from src.infra.middlewares.auth_wtf import auth_jwt_verify

users_route_bp = Blueprint("user_routes", __name__)


@users_route_bp.route("/users", methods=["POST"])
def create_user():
    try:
        body = request.json if isinstance(request.json, dict) else {}
        http_request = HttpRequest(body=body)
        view = create_user_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@users_route_bp.route("/sessions", methods=["POST"])
def authenticate_user():
    try:
        body = request.json if isinstance(request.json, dict) else {}
        http_request = HttpRequest(body=body)
        view = authenticate_user_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@users_route_bp.route("/test", methods=["GET"])
def auth():
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            token_infos=token_information,
            headers=request.headers
            )
        
        return jsonify(), 200
    except Exception as exception:
        return jsonify("Falha"), 500