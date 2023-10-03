from fastapi import APIRouter, status

from app.core.auth import bcrypt_context
from app.database import db_dependency
from app.users.schemas import CreateUserRequest, CreateUserResponse
from app.users.models import User

router = APIRouter(
    tags=['Users']
)


@router.post("/users/", response_model=CreateUserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserRequest, db: db_dependency):
    db_user = User(**user.dict())
    db_user.password = bcrypt_context.hash(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
