from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Integer, Boolean, LargeBinary, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.infra.database.postgre.settings.base import Base


class UserModel(Base):
    """
    Represents the User entity in the database.

    Attributes:
        id (UUID): Unique identifier for the user.
        email (str): The email address of the user.
        name (str): The full name of the user.
        nickname (str): The nickname or username of the user.
        password (str): The hashed password of the user.
        role (int): The role of the user (e.g., 1 for admin, 3 for regular users).
        active (bool): Indicates if the user's account is active.
        profile_photo (bytes): Binary data for the user's profile photo.
        created_at (datetime): The timestamp when the user was created.
        last_login (datetime): The timestamp of the user's last login.
    """

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(80), nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(Integer, nullable=False, default=3)
    active = Column(Boolean, nullable=False, default=True)
    profile_photo = Column(LargeBinary, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    last_login = Column(DateTime, nullable=True)
