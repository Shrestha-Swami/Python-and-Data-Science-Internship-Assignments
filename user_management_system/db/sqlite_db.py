import sqlite3
from db.base_db import BaseDB
from models.user import User
from config import SQLITE_DB_NAME

class SQLiteDB(BaseDB):
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_DB_NAME)
        self.conn.execute("PRAGMA foreign_keys = ON")

    def init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            username TEXT PRIMARY KEY,
                            password TEXT NOT NULL,
                            is_logged_in INTEGER DEFAULT 0
                        )''')
        cursor.execute("UPDATE users SET is_logged_in = 0")
        self.conn.commit()

    def add_user(self, user: User):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users(username, password, is_logged_in) VALUES (?, ?, ?)",
                       (user.username, user.password, user.is_logged_in))
        self.conn.commit()

    def get_user(self, username: str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT username, password, is_logged_in FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return User(*row) if row else None

    def update_login_status(self, username: str, status: int):
        self.conn.execute("UPDATE users SET is_logged_in = ? WHERE username = ?", (status, username))
        self.conn.commit()

    def update_password(self, username: str, hashed_password: str):
        self.conn.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
        self.conn.commit()

    def user_exists(self, username: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        return cursor.fetchone() is not None
