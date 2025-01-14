from src.domain.users.application.services.authenticate_user_service import (
    AuthenticateUserService,
)
from src.infra.controllers.interfaces.authenticate_user_controller_interface import (
    AuthenticateUserControllerInterface,
)


class AuthenticateUserController(AuthenticateUserControllerInterface):
    def __init__(self, authenticate_user_service: AuthenticateUserService) -> dict:
        self.__authenticate_user_service = authenticate_user_service

    def handle(self, email: str, password: str) -> None:
        """
        Handles the user creation process.

        Args:
            user_data (): The data required to authenticate a user.

        Raises:
            AlreadyExistsError: If the email or nickname is already in use.
            ResourceNotFoundError: If a required resource (e.g., admin user) is not found.
        """
        result = self.__authenticate_user_service.execute(email, password)

        if result.is_left():
            raise result.value
        
        return result.value
