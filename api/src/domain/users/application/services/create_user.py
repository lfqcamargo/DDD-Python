from typing import TypedDict
from src.domain.users.application.repositories.users_repository import UsersRepository
from src.domain.users.enterprise.entities.user import User

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

    def execute(self, data: CreateUserServiceRequest) -> None:
        """
        Executes the process of creating a new user.

        This method validates the input data, creates a new user entity,
        and saves it to the repository.

        Args:
            data (CreateUserServiceRequest): The data required to create a user.

        Returns:
            None
        """
        user = User.create(data)

        # Adiciona o usuário ao repositório
        self.users_repository.create(user)

        return True
