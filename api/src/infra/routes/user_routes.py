from flask import Blueprint, jsonify, request
from src.infra.views.http_types.http_request import HttpRequest
from src.infra.composer.create_user_composer import create_user_composer
from src.infra.errors.error_handle import handle_errors

users_route_bp = Blueprint("user_routes", __name__)


@users_route_bp.route("/users", methods=["POST"])
def create_user():
    """
    Handles the POST request to create a new user.

    This endpoint processes the HTTP request by validating the body,
    invoking the appropriate view and controller logic, and returning
    an HTTP response.

    Returns:
        Tuple[Response, int]: A tuple containing a Flask Response object with the
                              HTTP response body and the HTTP status code.

    Raises:
        Exception: Any unhandled exceptions are caught, processed via `handle_errors`,
                   and returned as a standardized HTTP response.
    """
    try:
        body = request.json if isinstance(request.json, dict) else {}
        http_request = HttpRequest(body=body)
        view = create_user_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
