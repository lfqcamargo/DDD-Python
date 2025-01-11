from abc import ABC, abstractmethod


class CreateUserControllerInterface(ABC):
    """
    Interface for the CreateUserController.

    This interface defines the contract for implementing a controller
    responsible for handling the creation of users. Any class that implements
    this interface must provide a concrete implementation for the `handle` method.
    """

    @abstractmethod
    def handle(self, user_data: dict) -> dict:
        """
        Handles the user creation process.

        This method should process the given user data and return a dictionary
        with the result of the user creation process.

        Args:
            user_data (dict): A dictionary containing the user's data required
                              for the creation process.

        Returns:
            dict: A dictionary containing the result of the user creation,
                  which may include user details, a success message, or error
                  information if the creation fails.
        """
