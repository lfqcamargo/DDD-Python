import pytest
from src.domain.users.application.services.authenticate_user_service import (
    AuthenticateUserService,
)
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.cryptography.fake_password import FakerPassword
from src.infra.drivers.jwt_handler import JwtHandler
from src.test.factories.make_user import make_user
from src.core.errors.resource_not_found_error import ResourNotFoundError


@pytest.fixture
def authenticate_user_service_fixture() -> (
    tuple[AuthenticateUserService, InMemoryUsersRepository]
):
    """
    Fixture to initialize the AuthenticateUserService with an InMemoryUsersRepository.

    Returns:
        AuthenticateUserService: A new instance of the service for each test.
    """
    user_repository = InMemoryUsersRepository()
    jwt_handler = JwtHandler()
    password_handler = FakerPassword()
    service = AuthenticateUserService(user_repository, jwt_handler, password_handler)
    return service, user_repository


def test_authenticate_user_success(authenticate_user_service_fixture):
    """
    Test the AuthenticateUserService for successful authentication.
    """
    service, user_repository = authenticate_user_service_fixture

    user = make_user(override={"password": "123456"})
    user_repository.items.append(user)

    result = service.execute(email=user.email, password="123456")
    print(result.value)

    assert result.is_right()
    response = result.value
    assert response["access"] is True
    assert response["email"] == user.email
    assert "token" in response
    assert isinstance(response["token"], str)


def test_authenticate_user_not_found(authenticate_user_service_fixture):
    """
    Test the AuthenticateUserService when the user is not found.
    """
    service, _ = authenticate_user_service_fixture

    # Tenta autenticar um usuário que não existe
    result = service.execute(email="notfound@example.com", password="123456")

    # Verifica o resultado
    assert result.is_left()
    assert isinstance(result.value, ResourNotFoundError)
    assert result.value.message == "User not found."


def test_authenticate_user_invalid_password(authenticate_user_service_fixture):
    """
    Test the AuthenticateUserService when the password is incorrect.
    """
    service, user_repository = authenticate_user_service_fixture

    # Cria um usuário
    user = make_user()
    user_repository.items.append(user)

    # Tenta autenticar com uma senha incorreta
    result = service.execute(email=user.email, password="wrongpassword")

    # Verifica o resultado
    assert result.is_left()
    assert isinstance(result.value, ResourNotFoundError)
    assert result.value.message == "User not found."
