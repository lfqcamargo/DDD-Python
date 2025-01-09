from src.domain.users.application.services.create_user import CreateUserService
from src.test.repositories.in_memory_users_repository import InMemoryUsersRepository
from src.test.factories.make_user import make_user

def test_create_user():
    """
    Test the CreateUserService to ensure it creates a user and adds it to the repository.
    """
    users_repository = InMemoryUsersRepository()
    create_user_service = CreateUserService(users_repository)

    user = make_user()

    create_user_service.execute({
        'email': user.email,
        'name': user.name,
        'nickname': user.nickname,
        'password': user.password,
        'role': user.role,
    })

    assert len(users_repository.items) == 1
    assert users_repository.items[0].email == user.email
    assert users_repository.items[0].id == 1
