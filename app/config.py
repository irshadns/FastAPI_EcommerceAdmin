import os

from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access configuration variables
# DATABASE CONFIG
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_ROOT_PASSWORD = os.getenv("DB_ROOT_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")

# AUTHENTICATION CONFIG
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = 'HS256'

# PAGINATION LIMIT
PAGINATION_LIMIT = 50
