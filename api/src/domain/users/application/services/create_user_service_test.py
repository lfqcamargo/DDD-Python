import pytest
from src.domain.users.application.services.create_user_service import CreateUserService
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_user import make_user
from src.core.errors.already_exists_error import AlreadyExistsError
from src.core.errors.resource_not_found_error import ResourNotFoundError
from src.domain.users.enterprise.entities.user import UserRole


@pytest.fixture
def user_service_fixture() -> tuple[CreateUserService, InMemoryUsersRepository]:
    """
    Fixture to initialize the CreateUserService with an InMemoryUsersRepository.

    Returns:
        CreateUserService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    create_user_service = CreateUserService(users_repository)
    return create_user_service, users_repository


def test_create_user(user_service_fixture):
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = user_service_fixture

    user = make_user()

    result = create_user_service.execute(
        {
            "email": user.email,
            "name": user.name,
            "nickname": user.nickname,
            "password": user.password,
            "role": UserRole.CUSTOMER,
        }
    )

    assert len(users_repository.items) == 1
    assert users_repository.items[0].email == user.email
    assert result.is_right()


def test_not_create_user_email(user_service_fixture):
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = user_service_fixture

    user = make_user()
    users_repository.items.append(user)

    result = create_user_service.execute(
        {
            "email": user.email,
            "name": user.name,
            "nickname": "lfqcamargo",
            "password": user.password,
            "role": UserRole.CUSTOMER,
        }
    )

    assert len(users_repository.items) == 1
    assert result.is_left()
    assert isinstance(result.value, AlreadyExistsError)
    assert result.value.message == "Email already exists."


def test_not_create_user_nickname(user_service_fixture):
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = user_service_fixture

    user = make_user()
    users_repository.items.append(user)

    result = create_user_service.execute(
        {
            "email": "lfqcamargo@gmail.com",
            "name": user.name,
            "nickname": user.nickname,
            "password": user.password,
            "role": UserRole.CUSTOMER,
        }
    )

    assert len(users_repository.items) == 1
    assert result.is_left()
    assert isinstance(result.value, AlreadyExistsError)
    assert result.value.message == "Nickname already exists."


def test_not_create_user_not_manager_if_not_admin(user_service_fixture):
    """It should not be possible to create a user other than a client
    without being an administrator"""
    create_user_service, users_repository = user_service_fixture

    user = make_user(override={"role": UserRole.ADMIN})

    result = create_user_service.execute(
        {
            "email": "lfqcamargo@gmail.com",
            "name": user.name,
            "nickname": user.nickname,
            "password": user.password,
            "role": user.role,
        }
    )

    assert len(users_repository.items) == 0
    assert result.is_left()
    assert isinstance(result.value, ResourNotFoundError)
    assert result.value.message == "User admin not found."
