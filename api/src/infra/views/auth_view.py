from src.infra.views.http_types.http_request import HttpRequest
from src.infra.views.http_types.http_response import HttpResponse
from src.infra.views.interfaces.view_interface import ViewInterface


class AuthView(ViewInterface):
    """
    Represents a view to handle HTTP requests for creating a user.
    """

    def __init__(self, controller) -> None:
        """
        Initializes the AuthView.
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

        user_data = http_request.body

        body_response = self.__controller.handle(user_data)

        return HttpResponse(status_code=201, body=body_response)
