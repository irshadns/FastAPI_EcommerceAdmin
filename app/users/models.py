from sqlalchemy import Boolean, Column, Integer, String, Enum

from app.database import Base
from app.users.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(30), unique=True)
    username = Column(String(30), unique=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    # hashed password
    password = Column(String(100), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.member)
    is_active = Column(Boolean, default=True)
