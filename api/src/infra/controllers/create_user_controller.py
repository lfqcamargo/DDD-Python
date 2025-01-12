from src.domain.users.application.services.create_user_service import (
    CreateUserService,
    CreateUserServiceRequest,
)
from src.infra.controllers.interfaces.create_user_controller_interface import (
    CreateUserControllerInterface,
)


class CreateUserController(CreateUserControllerInterface):
    def __init__(self, create_user_service: CreateUserService) -> None:
        self.__create_user_service = create_user_service

    def handle(self, user_data: CreateUserServiceRequest) -> None:
        """
        Handles the user creation process.

        Args:
            user_data (CreateUserServiceRequest): The data required to create a user.

        Raises:
            AlreadyExistsError: If the email or nickname is already in use.
            ResourceNotFoundError: If a required resource (e.g., admin user) is not found.
        """
        result = self.__create_user_service.execute(user_data)

        if result.is_left():
            raise result.value
