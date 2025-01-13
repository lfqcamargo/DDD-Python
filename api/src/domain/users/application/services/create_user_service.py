from uuid import UUID
from typing import TypedDict, Union, Optional
from src.domain.users.application.interfaces.users_interface import UsersInterface
from src.domain.users.enterprise.entities.user import User
from src.domain.users.enterprise.entities.user import UserRole
from src.core.either import left, right, Either
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.domain.users.application.interfaces.password_interface import PasswordInterface


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

    def __init__(
        self, users_repository: UsersInterface, password_driver: PasswordInterface
    ) -> None:
        """
        Initializes the CreateUserService with the specified user repository.

        Args:
            users_repository (UserRepository): The repository for managing user
            persistence.
        """
        self.users_repository = users_repository
        self.password_driver = password_driver

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

        validate_email = self.__find_user_email(data["email"])
        if validate_email is not None:
            return left(AlreadyExistsError("Email already exists.", "email"))

        validate_nickname = self.__find_user_nickname(data["nickname"])
        if validate_nickname is not None:
            return left(AlreadyExistsError("Nickname already exists.", "nickname"))

        validate_role = self.__validate_role(
            data.get("authenticate_user"), data["role"]
        )
        if not validate_role:
            return left(ResourNotFoundError("User admin not found.", "user"))

        data["password"] = self.password_driver.encrypt_password(data["password"])

        user = User.create(data)
        self.users_repository.create(user)

        return right(None)

    def __find_user_email(self, email: str) -> Optional[User]:
        user_email = self.users_repository.find_by_email(email)

        if user_email:
            return user_email

        return None

    def __find_user_nickname(self, nickname: str) -> Optional[User]:
        user_nickname = self.users_repository.find_by_nickname(nickname)

        if user_nickname:
            return user_nickname

        return None

    def __validate_role(
        self, authenticate_id: UUID = None, role: int = None
    ) -> False | True:
        if role is not None and role != UserRole.CUSTOMER:
            if not authenticate_id:
                return False

            user_authenticate = self.users_repository.find_by_id(authenticate_id)

            if not user_authenticate or not user_authenticate.is_admin():
                return False

        return True
