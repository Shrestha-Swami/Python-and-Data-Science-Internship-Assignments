from config import DB_TYPE
from db.sqlite_db import SQLiteDB
from db.postgres_db import PostgresDB
from services.user_service import UserService

def get_db():
    if DB_TYPE == "sqlite":
        return SQLiteDB()
    elif DB_TYPE == "postgres":
        return PostgresDB()
    else:
        raise ValueError("Unsupported DB type")

def main():
    db = get_db()
    db.init_db()
    service = UserService(db)
    present_user = None

    while True:
        print("\nUser Management Menu")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Logout")
        print("5. Exit")
        choice = input("Select option (1-5): ").strip()

        if choice == '1':
            service.register()
        elif choice == '2':
            present_user = service.login(present_user)
        elif choice == '3':
            service.change_password(present_user)
        elif choice == '4':
            present_user = service.logout(present_user)
        elif choice == '5':
            if present_user:
                service.logout(present_user)
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
