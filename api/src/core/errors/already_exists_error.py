class AlreadyExistsError(Exception):
    """
    Exception raised when a user with the same email or nickname already exists.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the AlreadyExistsError with a specific message.

        Args:
            message (str): The error message to describe the exception.
        """
        self.message = message
        super().__init__(message)
