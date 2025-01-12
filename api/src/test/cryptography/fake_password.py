from src.domain.users.application.interfaces.password_interface import PasswordInterface


class FakerPassword(PasswordInterface):
    def encrypt_password(self, password: str) -> str:
        return f"hashed_{password}"

    def check_password(self, password: str, hashed_password: str) -> bool:
        return hashed_password == f"hashed_{password}"
