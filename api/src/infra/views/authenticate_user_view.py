from src.infra.views.http_types.http_request import HttpRequest
from src.infra.views.http_types.http_response import HttpResponse
from src.infra.views.interfaces.view_interface import ViewInterface
from src.infra.controllers.interfaces.authenticate_user_controller_interface import (
    AuthenticateUserControllerInterface,
)
from src.infra.validators.authenticate_user_validator import authenticate_user_validator


class AuthenticateUserView(ViewInterface):
    """
    Represents a view to handle HTTP requests for creating a user.
    """

    def __init__(self, controller: AuthenticateUserControllerInterface) -> None:
        """
        Initializes the AuthenticateUserView.
        """
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """
        Handles the HTTP request for creating a user.

        Extracts the user data from the request body, invokes the controller to
        process the creation, and returns an HTTP response with the result.

        Args:
            http_request (HttpRequest): The HTTP request containing user data.

        Returns:
            HttpResponse: The HTTP response with status code and body containing
                          the result of the user creation process.
        """
        authenticate_user_validator(http_request)
        email = http_request.body.get("email")
        password = http_request.body.get("password")

        body_response = self.__controller.handle(email, password)

        return HttpResponse(status_code=200, body=body_response)
