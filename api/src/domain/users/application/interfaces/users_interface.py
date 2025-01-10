from uuid import UUID
from abc import ABC, abstractmethod
from src.domain.users.enterprise.entities.user import User


class UsersInterface(ABC):
    """
    Abstract base class for user interface.

    This class defines the contract for any repository implementation
    that handles user-related operations such as creating, finding,
    and retrieving user data.
    """

    @abstractmethod
    def create(self, user: User) -> None:
        """
        Abstract method to create a new user.

        This method must be implemented by any concrete subclass.
        It should handle the logic for persisting a user entity.

        Args:
            user: The user entity to be created.
        """

    @abstractmethod
    def find_by_id(self, id: UUID) -> User | None:
        """
        Abstract method to find a user by their unique ID.

        This method must be implemented by any concrete subclass.
        It should handle the logic for retrieving a user entity by its ID.

        Args:
            id (int): The unique identifier of the user.

        Returns:
            User: The user entity if found, or None if no user exists with the given ID.
        """

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """
        Abstract method to find a user by their email address.

        This method must be implemented by any concrete subclass.
        It should handle the logic for retrieving a user entity by its email.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user entity if found, or None if no user exists with the given email.
        """

    @abstractmethod
    def find_by_nickname(self, nickname: str) -> User | None:
        """
        Abstract method to find a user by their nickname.

        This method must be implemented by any concrete subclass.
        It should handle the logic for retrieving a user entity by its nickname.

        Args:
            nickname (str): The nickname of the user.

        Returns:
            User: The user entity if found, or None if no user exists with the given nickname.
        """
