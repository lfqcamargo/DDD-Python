from uuid import UUID
from src.domain.users.enterprise.entities.user import User
from src.infra.database.postgre.models.user_model import UserModel
from src.infra.database.postgre.mappers.user_mapper import SQLAlchemyUserMapper
from src.domain.users.application.interfaces.users_interface import UsersInterface


class UsersRepository(UsersInterface):
    """
    Repository implementation for handling User operations in the database.
    """

    def __init__(self, db_connection) -> None:
        """
        Initializes the UsersRepository with a database connection.

        Args:
            db_connection: A SQLAlchemy database connection.
        """
        self.__db_connection = db_connection

    def create(self, user: User) -> None:
        """
        Persists a new user in the database.

        Args:
            user (User): The user entity to persist.
        """
        with self.__db_connection as database:
            user_model_data = SQLAlchemyUserMapper.to_sqlalchemy(user)
            user_model = UserModel(**user_model_data)

            database.session.add(user_model)
            database.session.commit()

    def find_by_id(self, id: UUID) -> User | None:
        """
        Finds a user by their ID.

        Args:
            id (UUID): The user's unique identifier.

        Returns:
            User | None: The user entity if found, otherwise None.
        """
        with self.__db_connection as database:
            user_model = database.session.query(UserModel).filter_by(id=id).first()
            if user_model:
                return self.__to_domain(user_model)
            return None

    def find_by_email(self, email: str) -> User | None:
        """
        Finds a user by their email.

        Args:
            email (str): The user's email.

        Returns:
            User | None: The user entity if found, otherwise None.
        """
        with self.__db_connection as database:
            user_model = (
                database.session.query(UserModel).filter_by(email=email).first()
            )
            if user_model:
                return SQLAlchemyUserMapper().to_domain(user_model)
            return None

    def find_by_nickname(self, nickname: str) -> User | None:
        """
        Finds a user by their nickname.

        Args:
            nickname (str): The user's nickname.

        Returns:
            User | None: The user entity if found, otherwise None.
        """
        with self.__db_connection as database:
            user_model = (
                database.session.query(UserModel).filter_by(nickname=nickname).first()
            )
            if user_model:
                return self.__to_domain(user_model)
            return None

    @staticmethod
    def __to_domain(user_model: UserModel) -> User:
        """
        Maps a UserModel instance to a User entity.

        Args:
            user_model (UserModel): The UserModel instance to map.

        Returns:
            User: The corresponding domain entity.
        """
        return User.create(
            {
                "id": user_model.id,
                "name": user_model.name,
                "nickname": user_model.nickname,
                "email": user_model.email,
                "password": user_model.password,
                "role": user_model.role,
                "active": user_model.active,
                "profile_photo": user_model.profile_photo,
                "created_at": user_model.created_at,
                "last_login": user_model.last_login,
            },
        )
