from uuid import UUID
from src.domain.users.enterprise.entities.user import User
from src.infra.database.models.user_model import UserModel
from src.domain.users.application.interfaces.users_interface import UsersInterface


class UsersRepository(UsersInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create(self, user: User) -> None:
        print("CHEGOU NO CREATE REPOSITORY")
        print(self.__db_connection)
        with self.__db_connection as database:
            print("ENTROU NO WITH")
            print(user)
            user_model = UserModel(
                email = user.email, 
                name = user.name, 
                nickname = user.nickname, 
                password = user.password, 
                role = 3
            )
            database.session.add(user_model)
            print("DEPOIS DO ADD")
            database.session.commit()
            print("COMMIT")

    def find_by_id(self, id: UUID) -> User | None:
        return

    def find_by_email(self, email: str) -> User | None:
        return

    def find_by_nickname(self, nickname: str) -> User | None:
        return
        