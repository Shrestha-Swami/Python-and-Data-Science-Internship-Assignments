import getpass
from utils.security import hash_password, validate_password
from models.user import User
from db.base_db import BaseDB

class UserService:
    def __init__(self, db: BaseDB):
        self.db = db

    def register(self):
        username = input("Enter new username: ").strip()
        if not username:
            print("Username cannot be empty")
            return
        if self.db.user_exists(username):
            print("Username already exists")
            return
        password = getpass.getpass("Enter password: ")
        if not validate_password(password):
            return
        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match")
            return
        self.db.add_user(User(username, hash_password(password)))
        print("Registration successful")

    def login(self, present_user):
        if present_user:
            print(f"Already logged in as {present_user}")
            return present_user
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty")
            return None
        password = getpass.getpass("Enter password: ")
        user = self.db.get_user(username)
        if not user:
            print("Username not found")
            return None
        if user.is_logged_in:
            print("User already logged in")
            return None
        if hash_password(password) == user.password:
            self.db.update_login_status(username, 1)
            print(f"Logged in successfully: {username}")
            return username
        else:
            print("Incorrect password")
            return None

    def logout(self, present_user):
        if not present_user:
            print("No user logged in")
            return None
        self.db.update_login_status(present_user, 0)
        print(f"Logged out: {present_user}")
        return None

    def change_password(self, present_user):
        if not present_user:
            print("Login required to change password")
            return
        old_pass = getpass.getpass("Enter current password: ")
        user = self.db.get_user(present_user)
        if hash_password(old_pass) != user.password:
            print("Incorrect current password")
            return
        new_pass = getpass.getpass("Enter new password: ")
        if not validate_password(new_pass):
            return
        confirm_pass = getpass.getpass("Confirm new password: ")
        if new_pass != confirm_pass:
            print("Passwords do not match")
            return
        self.db.update_password(present_user, hash_password(new_pass))
        print("Password changed successfully")
