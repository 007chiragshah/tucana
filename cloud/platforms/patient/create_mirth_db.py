import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from app.settings import config as settings

DB_NAME = "mirthdb"


def create_db() -> None:
    print(f"Attempting creation DB: {DB_NAME}")
    connection = psycopg2.connect(
        user=settings.DB_USERNAME.get_secret_value(),
        password=settings.DB_PASSWORD.get_secret_value(),
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        dbname="postgres",
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Created DB: {DB_NAME}")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database {DB_NAME} already exists, skipping")
    finally:
        if connection:
            connection.close()
    print("Done creating DB")


if __name__ == "__main__":
    create_db()
    exit(0)
