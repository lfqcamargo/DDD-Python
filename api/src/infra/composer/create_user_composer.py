from src.infra.database.settings.connection import db_connection_handler
from src.infra.database.repositories.users_repository import UsersRepository
from src.infra.controllers.create_user_controller import CreateUserController
from src.domain.users.application.services.create_user_service import CreateUserService
from src.infra.views.create_user_views import CreateUserView


def create_user_composer():
    model = UsersRepository(db_connection_handler)
    service = CreateUserService(model)
    controller = CreateUserController(service)

    view = CreateUserView(controller)

    return view
