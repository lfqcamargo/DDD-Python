from src.infra.views.http_types.http_request import HttpRequest
from src.infra.views.http_types.http_response import HttpResponse
from src.infra.views.interfaces.view_interface import ViewInterface
from src.infra.controllers.interfaces.create_user_controller_interface import (
    CreateUserControllerInterface,
)
from src.infra.validators.create_user_validator import create_user_validator


class CreateUserView(ViewInterface):
    """
    Represents a view to handle HTTP requests for creating a user.
    """

    def __init__(self, controller: CreateUserControllerInterface) -> None:
        """
        Initializes the CreateUserView.
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
        create_user_validator(http_request)

        user_data = http_request.body

        body_response = self.__controller.handle(user_data)

        return HttpResponse(status_code=201, body=body_response)
