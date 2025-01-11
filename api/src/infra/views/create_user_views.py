from src.infra.views.http_types.http_request import HttpRequest
from src.infra.views.http_types.http_response import HttpResponse
from src.infra.views.interfaces.view_interface import ViewInterface
from src.infra.controllers.interfaces.create_user_controller_interface import CreateUserControllerInterface

class CreateUserView(ViewInterface):
    def __init__(self, controller: CreateUserControllerInterface) -> None:
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        user_data = http_request.body
        
        print("CHEGOU NA VIEW CREATEUSER")
        body_response = self.__controller.handle(user_data)

        return HttpResponse(status_code=201, body=body_response)