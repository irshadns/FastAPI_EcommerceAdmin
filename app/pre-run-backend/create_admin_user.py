import os

from dotenv import load_dotenv

from app.core.auth import bcrypt_context
from app.database import SessionLocal
from app.users.enums import UserRole
from app.users.models import User

# Load the environment variables from the .env file
load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_FIRSTNAME = os.getenv("ADMIN_FIRSTNAME")
ADMIN_LASTNAME = os.getenv("ADMIN_LASTNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def create_admin_user():
    db = SessionLocal()
    user = User(
        email=ADMIN_EMAIL,
        username=ADMIN_USERNAME,
        first_name=ADMIN_FIRSTNAME,
        last_name=ADMIN_LASTNAME,
        password=bcrypt_context.hash(ADMIN_PASSWORD),
        role=UserRole.admin.value
    )
    db.add(user)
    db.commit()
    db.close()
    print(
        f"********** Admin User has been created with username:{ADMIN_USERNAME} password:{ADMIN_PASSWORD} email:{ADMIN_EMAIL} **********")


if __name__ == '__main__':
    create_admin_user()
