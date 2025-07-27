import psycopg2
from db.base_db import BaseDB
from models.user import User
from config import POSTGRES_CONFIG

class PostgresDB(BaseDB):
    def __init__(self):
        self.conn = psycopg2.connect(**POSTGRES_CONFIG)
        self.conn.autocommit = True

    def init_db(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                username VARCHAR(50) PRIMARY KEY,
                                password TEXT NOT NULL,
                                is_logged_in INT DEFAULT 0
                              )''')
            cursor.execute("UPDATE users SET is_logged_in = 0")

    def add_user(self, user: User):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users(username, password, is_logged_in) VALUES (%s, %s, %s)",
                (user.username, user.password, user.is_logged_in)
            )

    def get_user(self, username: str):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT username, password, is_logged_in FROM users WHERE username = %s",
                (username,)
            )
            row = cursor.fetchone()
            return User(*row) if row else None

    def update_login_status(self, username: str, status: int):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET is_logged_in = %s WHERE username = %s",
                (status, username)
            )

    def update_password(self, username: str, hashed_password: str):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET password = %s WHERE username = %s",
                (hashed_password, username)
            )

    def user_exists(self, username: str) -> bool:
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
            return cursor.fetchone() is not None
