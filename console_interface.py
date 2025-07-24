import getpass
import sqlite3
import hashlib

DB_NAME = "user_management.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        is_logged_in INTEGER DEFAULT 0
                      )''')
    cursor.execute("UPDATE users SET is_logged_in = 0")
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()  #Return SHA-256 hash of the given password

def user_exists(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = ?", (username,)) #Take a tuple with one element
    res = cursor.fetchone()
    conn.close()
    return res is not None
    #return True if the record is found else false

# Fetches user record by username
def get_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, is_logged_in FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# Update login status of a user
def update_login_status(username, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET is_logged_in = ? WHERE username = ?", (status, username))
    conn.commit()
    cursor.close()

#Updates user password to new hashed password
def update_password(username, new_hashed_password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_hashed_password, username))
    conn.commit()
    conn.close()
def validate_password(password):
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return False
    if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        print("Password must contain both letters and numbers!")
        return False
    return True

# Console Functions
def register():
    username = input("Enter new username: ").strip()
    if not username:
        print("Username cannot be empty!")
        return
    if user_exists(username):
        print("Username already exists! Try again with a new username.")
        return
    password = getpass.getpass("Enter password: ")
    if not validate_password(password):
        return
    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Password and confirm passwords do not match.")
        return
    hashed_password = hash_password(password)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT into users(username, password, is_logged_in) VALUES (?, ?, 0)", (username, hashed_password))
    conn.commit()
    conn.close()
    print("Registration Successful!")

def login(present_user):
    if present_user:
        print(f"Already logged in as {present_user}. Logout first") #Prevents user who is already logged_in
        return present_user
    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty!")
        return
    password = getpass.getpass("Enter password: ")
    if not password:
        print("Password cannot be empty!")
        return None
    user = get_user(username)

    if not user:
        print("Username not found!")
        return None
    stored_username, stored_password, is_logged_in = user
    if is_logged_in:
        print("User is already logged in from another session!")
        return None
    
    if hash_password(password) == stored_password:
        update_login_status(username, 1)
        print(f"Logged in successfully! Welcome, {username}.")
        return username
    else:
        print("Incorrect password!")
        return None

def logout(present_user):
    if not present_user:
        print("No user is currently logged in!")
        return None
    update_login_status(present_user, 0)
    print(f"{present_user} has been successfully logged out.")
    return None

def change_password(present_user):
    if not present_user:
        print("You must be logged in to change your password!")
        return
    old_pass = getpass.getpass("Enter current password: ")
    if not old_pass:
        print("Current password cannot be empty!")
        return
    user = get_user(present_user)
    if not user:
        print("Error in fetching user data!")
        return
    if hash_password(old_pass) != user[1]:
        print("Incorrect current password!")
        return
    new_pass = getpass.getpass("Enter new password: ")
    if not validate_password(new_pass):
        return
    confirm_pass = getpass.getpass("Confirm new password: ")
    
    if new_pass != confirm_pass:
        print("Passwords do not match!")
        return
    update_password(present_user, hash_password(new_pass))
    print("Password changed successfully!")

# Menu System
def main_menu():
    init_db()
    present_user = None
    while True:
        print("\n-----USER MANAGEMENT MENU-----")
        print("1. Register")
        print("2. Login")
        print("3. Change Password")
        print("4. Logout")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            register()
        elif choice == '2':
            present_user = login(present_user)
        elif choice == '3':
            change_password(present_user)
        elif choice == '4':
            present_user = logout(present_user)
        elif choice == '5':
            if present_user:
                logout(present_user)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main_menu()