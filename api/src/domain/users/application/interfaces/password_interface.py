from abc import ABC, abstractmethod


class PasswordInterface(ABC):

    @abstractmethod
    def encrypt_password(self, password: str) -> str:
        pass

    @abstractmethod
    def check_password(self, password: str, hashed_password: str) -> str:
        pass
