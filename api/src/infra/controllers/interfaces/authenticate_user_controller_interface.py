from abc import ABC, abstractmethod


class AuthenticateUserControllerInterface(ABC):

    @abstractmethod
    def handle(self, email: str, password: str) -> dict:
        pass
