from typing import Optional

from pydantic import BaseModel

from app.users.enums import UserRole


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    role: str
    is_active: bool

    class Config:
        orm_mode = True


class CreateUserBase(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str


class CreateUserRequest(CreateUserBase):
    password: str


class CreateUserResponse(CreateUserBase):
    role: str

    class Config:
        orm_mode = True
