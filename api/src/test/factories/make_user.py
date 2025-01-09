from typing import Optional, Dict
from faker import Faker
from src.domain.users.enterprise.entities.user import User
from src.domain.users.enterprise.entities.user import UserProps


faker = Faker()
# pylint: disable=redefined-builtin
def make_user(override: Optional[Dict] = None, id: Optional[int] = None) -> User:
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
        "id": id or 0,  # Default ID is 0
        "email": faker.email(),
        "name": faker.name(),
        "nickname": faker.user_name(),
        "password": faker.password(),
        "role": faker.random_int(min=1, max=2),  # Random role between 1 and 2
        "active": faker.boolean(),
        "profile_photo": None,
        "created_at": faker.date_time(),
        "last_login": None,
    }

    # Merge default properties with any overrides provided
    final_props = {**default_props, **(override or {})}

    # Create the user instance
    user = User.create(final_props)

    return user
