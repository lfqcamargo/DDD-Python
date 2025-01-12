from src.infra.database.postgre.models.user_model import UserModel


class UserPresenter:
    """
    Presenters Users
    """

    @staticmethod
    def to_http(user: UserModel):
        """
        Presenter to HTTP
        """
        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "nickname": user.nickname,
            "role": user.role,
            "active": user.active,
            "profile_photo": user.profile_photo,
            "created_at": user.created_at,
            "last_login": user.last_login,
        }
