from .password_handler import PasswordHandler


def test_encrypt():
    minha_senha = "123456789"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(minha_senha)
    password_checked = password_handler.check_password(minha_senha, hashed_password)

    assert password_checked
