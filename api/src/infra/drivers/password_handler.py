import bcrypt
from src.domain.users.application.interfaces.password_interface import PasswordInterface


class PasswordHandler(PasswordInterface):
    def encrypt_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password

    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
