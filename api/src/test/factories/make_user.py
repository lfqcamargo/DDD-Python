from uuid import uuid4
from typing import Optional, Dict, Any, cast
from faker import Faker
from src.domain.users.enterprise.entities.user import User
from src.domain.users.enterprise.entities.user import UserProps
from src.domain.users.enterprise.entities.user import UserRole
from src.test.cryptography.fake_password import FakerPassword

faker = Faker()


# pylint: disable=redefined-builtin
def make_user(override: Optional[Dict[str, Any]] = None) -> User:
    """
    Creates a User object with default values, allowing overrides for specific attributes.

    This function generates default user properties using Faker and merges them
    with any provided overrides. It creates a User instance with the combined properties.

    Args:
        override (Optional[Dict]): A dictionary of properties to override the default values.
        id (Optional[int]): The ID of the user. If not provided, defaults to 0.

    Returns:
        User: The created User instance with the provided or default properties.
    """
    default_props: UserProps = {
        "id": uuid4(),
        "email": faker.email(),
        "name": faker.name(),
        "nickname": faker.user_name(),
        "password": faker.password(),
        "role": UserRole.MANAGER,  # Default role is USER
        "active": faker.boolean(),
        "profile_photo": None,
        "created_at": faker.date_time(),
        "last_login": None,
    }

    # Merge default properties with any overrides provided
    final_props: UserProps = cast(UserProps, {**default_props, **(override or {})})
    
    encrypter_password = FakerPassword()
    final_props["password"] = encrypter_password.encrypt_password(final_props["password"])

    # Create the user instance
    user = User.create(final_props)

    return user
