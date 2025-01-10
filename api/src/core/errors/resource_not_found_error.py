class ResourNotFoundError(Exception):
    """
    Exception raised when a resource not found.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the ResourNotFoundError with a specific message.

        Args:
            message (str): The error message to describe the exception.
        """
        self.message = message
        super().__init__(message)
