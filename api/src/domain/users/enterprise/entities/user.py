from datetime import datetime
from typing import TypedDict, Optional

class UserProps(TypedDict):
    """
    Defines the properties required to create a User entity.
    """
    id: int
    email: str
    name: str
    nickname: str
    password: str
    role: str
    active: bool
    profile_photo: Optional[bytes]
    created_at: datetime
    last_login: Optional[datetime]

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
        self.id: int = props['id']
        self.email: str = props['email']
        self.name: str = props['name']
        self.nickname: str = props['nickname']
        self.password: str = props['password']
        self.role: str = props['role']
        self.active: bool = props['active']
        self.profile_photo: Optional[bytes] = props.get('profile_photo')
        self.created_at: datetime = props['created_at']
        self.last_login: Optional[datetime] = props.get('last_login')

    def to_dict(self) -> dict:
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

    @staticmethod
    def create(props: dict) -> 'User':
        """
        Creates a new User instance using the provided properties.

        If `created_at` is not provided, the current datetime will be used.
        Default values for `id` and `active` are assigned if not provided.

        Args:
            props (dict): Dictionary containing user attributes.

        Returns:
            User: A new User instance.
        """
        props.setdefault('id', 0)
        props.setdefault('active', True)
        props['created_at'] = props.get('created_at', datetime.now())

        return User(props)
