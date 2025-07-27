from abc import ABC, abstractmethod
from models.user import User

class BaseDB(ABC):
    @abstractmethod
    def init_db(self):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, username: str) -> User:
        pass

    @abstractmethod
    def update_login_status(self, username: str, status: int):
        pass

    @abstractmethod
    def update_password(self, username: str, hashed_password: str):
        pass

    @abstractmethod
    def user_exists(self, username: str) -> bool:
        pass
