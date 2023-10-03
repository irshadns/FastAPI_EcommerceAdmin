from datetime import timedelta, datetime
from functools import wraps
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette import status

from app.config import JWT_SECRET_KEY, ALGORITHM
from app.core.schemas import Token
from app.database import db_dependency
from app.users.enums import UserRole
from app.users.models import User

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def authenticate_user(username: str, password: str, db):
    print(f"authenticate_user USERNAME :: {username} PASSWORD {password}")
    if user := db.query(User).filter(User.username == username).first():
        return (
            user if bcrypt_context.verify(password, user.password) else False
        )
    return False


def has_admin_permission(role: str):
    return role == UserRole.admin


def get_unauthorized_response():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate user.',
    )


def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    expires = datetime.utcnow() + expires_delta
    encode = {'sub': username, 'id': user_id, 'role': role, 'exp': expires}
    return jwt.encode(encode, JWT_SECRET_KEY, algorithm=ALGORITHM)


async def get_admin_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        print(f"get_current_user TOKEN :: {token}")
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if not username or not user_id:
            raise get_unauthorized_response()
        user_role: str = payload.get('role')
        return user_role == UserRole.admin
    except JWTError as exc:
        raise get_unauthorized_response() from exc


# Custom Dependency for Authentication & Authorization of Admin User
admin_dependency = Annotated[dict, Depends(get_admin_user)]


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise get_unauthorized_response()
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}
