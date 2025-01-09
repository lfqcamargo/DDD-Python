from typing import TypedDict, Union
from src.domain.users.application.repositories.users_repository import UsersRepository
from src.domain.users.enterprise.entities.user import User
from src.core.either import left, right, Either
from src.core.errors.already_exists_error import AlreadyExistsError

class CreateUserServiceRequest(TypedDict):
    """
    TypedDict defining the structure for the data required to create a user.

    Attributes:
        email (str): The user's email address.
        name (str): The user's full name.
        nickname (str): The user's nickname or username.
        password (str): The user's password.
        role (str): The role assigned to the user (e.g., admin, user).
    """
    email: str
    name: str
    nickname: str
    password: str
    role: str

class CreateUserService():
    """
    Service class responsible for handling user creation logic.

    Attributes:
        users_repository (UserRepository): The repository for managing user persistence.
    """
    def __init__(self, users_repository: UsersRepository) -> None:
        """
        Initializes the CreateUserService with the specified user repository.

        Args:
            users_repository (UserRepository): The repository for managing user 
            persistence.
        """
        self.users_repository = users_repository

    def execute(self, data: CreateUserServiceRequest) -> Either[Union[AlreadyExistsError], None]:
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
        user_email = self.users_repository.find_by_email(data['email'])

        if user_email:
            return left(AlreadyExistsError("Email already exists."))

        user_nickname = self.users_repository.find_by_nickname(data['nickname'])

        if user_nickname:
            return left(AlreadyExistsError("Nickname already exists."))

        user = User.create(data)

        self.users_repository.create(user)

        return right(None)
