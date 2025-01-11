from uuid import UUID, uuid4

from datetime import datetime
from typing import TypedDict, Optional, Dict, Union
from enum import Enum


class UserRole(int, Enum):
    """
    Enum representing the possible roles for a user.
    """

    ADMIN = 1
    MANAGER = 2
    CUSTOMER = 3


class UserProps(TypedDict):
    """
    Defines the properties required to create a User entity.
    """

    id: UUID
    email: str
    name: str
    nickname: str
    password: str
    role: UserRole
    active: bool
    profile_photo: Optional[bytes]
    created_at: datetime
    last_login: Optional[datetime]


class CreateUserProps(TypedDict):
    """_
    Defines create user
    """

    email: str
    name: str
    nickname: str
    password: str
    role: UserRole


class User:
    """
    Represents a user entity in the system.
    Provides methods to create and serialize a User.
    """

    def __init__(self, props: UserProps) -> None:
        """
        Initializes a User instance with the given properties.

        Args:
            props (UserProps): Dictionary containing user attributes.
        """
        self.id: UUID = props["id"]
        self.email: str = props["email"]
        self.name: str = props["name"]
        self.nickname: str = props["nickname"]
        self.password: str = props["password"]
        self.role: int = props["role"]
        self.active: bool = props["active"]
        self.profile_photo: Optional[bytes] = props.get("profile_photo")
        self.created_at: datetime = props["created_at"]
        self.last_login: Optional[datetime] = props.get("last_login")

    def to_dict(self) -> Dict[str, Union[str, int, bool, bytes, None]]:
        """
        Converts the User instance into a dictionary.

        Returns:
            dict: A dictionary representation of the User instance.
        """
        return {
            "id": str(self.id),
            "email": self.email,
            "name": self.name,
            "nickname": self.nickname,
            "role": self.role,
            "active": self.active,
            "profile_photo": self.profile_photo,
            "created_at": self.created_at.isoformat(),
            "last_login": self.last_login.isoformat() if self.last_login else None,
        }

    def is_admin(self) -> bool:
        """
        Checks if the user has the role of an administrator.

        This method evaluates whether the user's role is set to UserRole.ADMIN.

        Returns:
            bool: True if the user is an administrator, False otherwise.
        """
        if self.role == UserRole.ADMIN:
            return True
        return False

    @staticmethod
    def create(props: CreateUserProps) -> "User":
        """
        Creates a new User instance using the provided properties.

        If created_at is not provided, the current datetime will be used.
        Default values for id and active are assigned if not provided.

        Args:
            props (dict): Dictionary containing user attributes.

        Returns:
            User: A new User instance.
        """

        user: UserProps = {
            "id": uuid4(),
            "email": props["email"],
            "name": props["name"],
            "nickname": props["nickname"],
            "password": props["password"],
            "role": props["role"],
            "active": True,
            "profile_photo": None,
            "created_at": datetime.now(),
            "last_login": None,
        }

        return User(user)
