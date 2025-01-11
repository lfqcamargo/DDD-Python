from src.domain.users.application.services.create_user_service import CreateUserServiceRequest
from src.infra.controllers.interfaces.create_user_controller_interface import CreateUserControllerInterface

class CreateUserController(CreateUserControllerInterface):
    def __init__(self, create_user_service) -> None:
        self.__create_user_service = create_user_service
        
    def handle(self, create_user_props: CreateUserServiceRequest) -> None:
        print("CHEGOU NO CONTROLLER")
        self.__create_user_service.execute(create_user_props)