from flask import Blueprint, jsonify, request
from src.infra.views.http_types.http_request import HttpRequest
from src.infra.composer.create_user_composer import create_user_composer

users_route_bp = Blueprint("user_routes", __name__)

@users_route_bp.route("/users", methods=["POST"])
def create_user():
    try:
        
        http_request = HttpRequest(body=request.json)
        
        view = create_user_composer()
        
        print("CHEGOU NA ROTA")
        http_response = view.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        print(exception)
        #http_response = handle_errors(exception)
        #return jsonify(http_response.body), http_response.status_code
        return jsonify(exception), 500