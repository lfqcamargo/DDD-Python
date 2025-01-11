from uuid import UUID
from typing import TypedDict, Union, Optional
from src.domain.users.application.interfaces.users_interface import UsersInterface
from src.domain.users.enterprise.entities.user import User
from src.domain.users.enterprise.entities.user import UserRole
from src.core.either import left, right, Either
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourNotFoundError


class CreateUserServiceRequest(TypedDict):
    """
    TypedDict defining the structure for the data required to create a user.

    Attributes:
        authenticate_user (uuid): The user's authenticate in system.
        email (str): The user's email address.
        name (str): The user's full name.
        nickname (str): The user's nickname or username.
        password (str): The user's password.
        role (str): The role assigned to the user (e.g., admin, user).
    """

    authenticate_user: Optional[UUID]
    email: str
    name: str
    nickname: str
    password: str
    role: UserRole


class CreateUserService:
    """
    Service class responsible for handling user creation logic.

    Attributes:
        users_repository (UserRepository): The repository for managing user persistence.
    """

    def __init__(self, users_repository: UsersInterface) -> None:
        """
        Initializes the CreateUserService with the specified user repository.

        Args:
            users_repository (UserRepository): The repository for managing user
            persistence.
        """
        self.users_repository = users_repository

    def execute(
        self, data: CreateUserServiceRequest
    ) -> Either[Union[AlreadyExistsError, ResourNotFoundError], None]:
        """
        Executes the process of creating a new user.

        This method validates the input data, creates a new user entity,
        and saves it to the repository.

        Args:
            data (CreateUserServiceRequest): The data required to create a user.

        Returns:
            Either[Union[AlreadyExistsError, ResourceNotFoundError], None]:
                - Left: An error if the email or nickname already exists.
                - Right: None if the user is successfully created.
        """
        print("CHEGOU NO SERVIÇO")
        user_email = self.users_repository.find_by_email(data["email"])

        if user_email:
            return left(AlreadyExistsError("Email already exists."))

        user_nickname = self.users_repository.find_by_nickname(data["nickname"])

        if user_nickname:
            return left(AlreadyExistsError("Nickname already exists."))

        """
        if data["role"] != UserRole.MANAGER:
            print("CHEGOU NO FINAL DO SERVIÇO")
            authenticate_user = data.get("authenticate_user")

            if not authenticate_user:
                return left(ResourNotFoundError("User admin not found."))

            user_authenticate = self.users_repository.find_by_id(authenticate_user)

            if not user_authenticate or not user_authenticate.is_admin():
                return left(ResourNotFoundError("User admin not found."))
        """

        user = User.create(data)

        self.users_repository.create(user)

        return right(None)
