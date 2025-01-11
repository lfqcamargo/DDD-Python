from src.domain.users.application.services.create_user_service import (
    CreateUserService, CreateUserServiceRequest,
)
from src.infra.controllers.interfaces.create_user_controller_interface import (
    CreateUserControllerInterface,
)


class CreateUserController(CreateUserControllerInterface):
    def __init__(self, create_user_service: CreateUserService) -> None:
        self.__create_user_service = create_user_service

    def handle(self, user_data: CreateUserServiceRequest) -> None:
        self.__create_user_service.execute(user_data)
