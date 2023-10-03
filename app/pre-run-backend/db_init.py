import pymysql

from app.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_ROOT_PASSWORD

# MySQL database configuration
db_config = {
    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASSWORD,
}

# Create the "mydb" database if it doesn't exist
create_database_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

# Backup Query if you face any issue with PRIVILEGES, uncomment below code & run it.
# create_database_query = f"""
# CREATE DATABASE {DB_NAME};
# CREATE USER 'ecommerce_user'@'{DB_HOST}' IDENTIFIED BY '{DB_ROOT_PASSWORD}';
# GRANT ALL PRIVILEGES ON {DB_NAME}.* TO '{DB_USER}'@'{DB_HOST}';
# """

print(f"***** Initializing MySQL Database '{DB_NAME}' ******")
try:
    with pymysql.connect(**db_config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_database_query)
    print(f"***** MySQL Database '{DB_NAME}' created successfully *****")
except pymysql.Error as err:
    print(f"Error Initializing MySQL Database '{DB_NAME} : {err}")
