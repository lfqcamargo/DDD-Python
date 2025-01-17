from src.infra.database.postgre.settings.connection import db_connection_handler
from src.infra.database.postgre.repositories.users_repository import UsersRepository
from src.infra.controllers.create_user_controller import CreateUserController
from src.domain.users.application.services.create_user_service import CreateUserService
from src.infra.views.create_user_views import CreateUserView
from src.infra.drivers.password_handler import PasswordHandler


def create_user_composer():
    """
    Compose to create user
    """
    model = UsersRepository(db_connection_handler)
    password_handler = PasswordHandler()
    service = CreateUserService(model, password_handler)
    controller = CreateUserController(service)

    view = CreateUserView(controller)

    return view
