import pytest
from src.domain.users.application.services.create_user import CreateUserService
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_user import make_user
from src.core.errors.already_exists_error import AlreadyExistsError

@pytest.fixture
def create_user_service_fixture():
    """
    Fixture to initialize the CreateUserService with an InMemoryUsersRepository.
    
    Returns:
        CreateUserService: A new instance of the service for each test.
    """
    users_repository = InMemoryUsersRepository()
    create_user_service = CreateUserService(users_repository)
    return create_user_service, users_repository

def test_create_user(create_user_service_fixture):
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = create_user_service_fixture

    user = make_user()

    result = create_user_service.execute({
        'email': user.email,
        'name': user.name,
        'nickname': user.nickname,
        'password': user.password,
        'role': user.role,
    })

    assert len(users_repository.items) == 1
    assert users_repository.items[0].email == user.email
    assert users_repository.items[0].id == 1
    assert result.is_right()

def test_not_create_user_email(create_user_service_fixture):
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = create_user_service_fixture

    user = make_user()
    users_repository.items.append(user)

    result = create_user_service.execute({
        'email': user.email,
        'name': user.name,
        'nickname': 'lfqcamargo',
        'password': user.password,
        'role': user.role,
    })

    assert len(users_repository.items) == 1
    assert result.is_left()
    assert isinstance(result.value, AlreadyExistsError)
    assert result.value.message == "Email already exists."

def test_not_create_user_nickname(create_user_service_fixture):
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    create_user_service, users_repository = create_user_service_fixture

    user = make_user()
    users_repository.items.append(user)

    result = create_user_service.execute({
        'email': 'lfqcamargo@gmail.com',
        'name': user.name,
        'nickname': user.nickname,
        'password': user.password,
        'role': user.role,
    })

    assert len(users_repository.items) == 1
    assert result.is_left()
    assert isinstance(result.value, AlreadyExistsError)
    assert result.value.message == "Nickname already exists."
