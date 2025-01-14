from src.infra.database.postgre.settings.connection import db_connection_handler
from src.infra.database.postgre.repositories.users_repository import UsersRepository
from src.infra.controllers.authenticate_user_controller import (
    AuthenticateUserController,
)
from src.domain.users.application.services.authenticate_user_service import (
    AuthenticateUserService,
)
from src.infra.views.authenticate_user_view import AuthenticateUserView
from src.infra.drivers.password_handler import PasswordHandler
from src.infra.drivers.jwt_handler import JwtHandler


def authenticate_user_composer():
    """
    Compose to authenticate user
    """
    model = UsersRepository(db_connection_handler)
    password_handler = PasswordHandler()
    jwt_handler = JwtHandler()
    service = AuthenticateUserService(model, jwt_handler, password_handler)
    controller = AuthenticateUserController(service)

    view = AuthenticateUserView(controller)

    return view
