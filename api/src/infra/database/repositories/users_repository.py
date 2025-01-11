from uuid import UUID
from src.domain.users.enterprise.entities.user import User
from src.infra.database.models.user_model import UserModel
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
            user_model = UserModel(
                id=user.id,
                email=user.email,
                name=user.name,
                nickname=user.nickname,
                password=user.password,
                role=user.role,
                active=user.active,
                profile_photo=user.profile_photo,
                created_at=user.created_at,
                last_login=user.last_login,
            )
            database.session.add(user_model)
            print("DEPOIS DO ADD")
            database.session.commit()
            print("COMMIT")

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
            user_model = database.session.query(UserModel).filter_by(email=email).first()
            if user_model:
                return self.__to_domain(user_model)
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
            user_model = database.session.query(UserModel).filter_by(nickname=nickname).first()
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
