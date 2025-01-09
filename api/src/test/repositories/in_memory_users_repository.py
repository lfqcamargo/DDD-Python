from src.domain.users.enterprise.entities.user import User
from src.domain.users.application.repositories.users_repository import UsersRepository

class InMemoryUsersRepository(UsersRepository):
    """
    In-memory implementation of the UserRepository for testing purposes.
    
    This class provides an in-memory storage mechanism for user entities,
    useful for unit testing without relying on a database.
    """

    def __init__(self):
        """
        Initializes the in-memory user repository.

        Attributes:
            items (list): List to store user entities.
            current_id (int): Counter to generate unique user IDs.
        """
        self.items = []
        self.current_id = 1

    def create(self, user: User) -> None:
        """
        Creates a new user in the in-memory repository.

        If the user's ID is 0 (default), assigns a new unique ID before adding it
        to the repository.

        Args:
            user (User): The user entity to be created.
        """
        if user.id == 0:
            user.id = self.current_id
            self.current_id += 1

        self.items.append(user)

    def find_by_id(self, id: int) -> User:
        """
        Finds a user by their unique ID.

        Args:
            id (int): The unique identifier of the user.

        Returns:
            User: The user entity if found, or None if no user exists with the given ID.
        """
        return next((user for user in self.items if user.id == id), None)

    def find_by_email(self, email: str) -> User:
        """
        Finds a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user entity if found, or None if no user exists with the given email.
        """
        return next((user for user in self.items if user.email == email), None)

    def find_by_nickname(self, nickname: str) -> User:
        """
        Finds a user by their nickname.

        Args:
            nickname (str): The nickname of the user.

        Returns:
            User: The user entity if found, or None if no user exists with the given nickname.
        """
        return next((user for user in self.items if user.nickname == nickname), None)
