from typing import Dict, Any
from src.domain.users.enterprise.entities.user import User
from src.infra.database.postgre.models.user_model import UserModel


class SQLAlchemyUserMapper:
    """
    Mapper User
    """

    @staticmethod
    def to_domain(raw: UserModel) -> User:
        """
        Maps a SQLAlchemy UserModel to a domain User entity.

        Args:
            raw (UserModel): The SQLAlchemy user model instance.

        Returns:
            User: The domain user entity.
        """
        return User.create(
            {
                "name": raw.name,
                "nickname": raw.nickname,
                "email": raw.email,
                "password": raw.password,
                "role": raw.role,
                "active": raw.active,
                "profile_photo": raw.profile_photo,
                "created_at": raw.created_at,
                "last_login": raw.last_login,
            }
        )

    @staticmethod
    def to_sqlalchemy(user: User) -> Dict[str, Any]:
        """
        Maps a domain User entity to a SQLAlchemy UserModel dictionary.

        Args:
            user (User): The domain user entity.

        Returns:
            Dict[str, Any]: A dictionary suitable for creating a SQLAlchemy UserModel.
        """
        return {
            "id": user.id,
            "name": user.name,
            "nickname": user.nickname,
            "email": user.email,
            "password": user.password,
            "role": user.role,
            "active": user.active,
            "profile_photo": user.profile_photo,
            "created_at": user.created_at,
            "last_login": user.last_login,
        }
