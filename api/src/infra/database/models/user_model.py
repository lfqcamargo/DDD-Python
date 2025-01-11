from sqlalchemy import Column, String, Integer, Boolean, LargeBinary, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from src.infra.database.settings.base import Base
from uuid import uuid4

class UserModel(Base):
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