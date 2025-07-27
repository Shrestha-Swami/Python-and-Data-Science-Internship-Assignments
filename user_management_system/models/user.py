class User:
    def __init__(self, username: str, password: str, is_logged_in: int = 0):
        self.username = username
        self.password = password  # hashed password
        self.is_logged_in = is_logged_in
