from uuid import UUID
from typing import Union, Optional
from src.domain.users.application.interfaces.users_interface import UsersInterface
from src.domain.users.enterprise.entities.user import User
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.core.either import left, right, Either
from src.domain.users.application.interfaces.password_interface import PasswordInterface
from src.infra.drivers.jwt_handler import JwtHandler


class AuthenticateUserService:
    def __init__(
        self,
        user_repository: UsersInterface,
        jwt_handler: JwtHandler,
        password_handler: PasswordInterface,
    ) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = jwt_handler
        self.__password_handler = password_handler

    def execute(
        self, email: str, password: str
    ) -> Either[Union[ResourNotFoundError], None]:
        user = self.__find_user(email)

        if user is None:
            return left(ResourNotFoundError("User not found.", "user"))

        is_password_valid = self.__password_handler.check_password(
            password, user.password
        )
    

        if not is_password_valid:
            return left(ResourNotFoundError("User not found.", "password"))

        token = self.__create_jwt_token(user.id)
        return right(self.__format_response(email, token))

    def __find_user(self, email: str) -> Optional[User]:
        user = self.__user_repository.find_by_email(email)

        if user:
            return user

        return None

    def __create_jwt_token(self, id: UUID) -> str:
        payload = {"id": str(id)}
        token = self.__jwt_handler.create_jwt_token(payload)
        return token

    def __format_response(self, email: str, token: str) -> dict:
        return {"access": True, "email": email, "token": token}
