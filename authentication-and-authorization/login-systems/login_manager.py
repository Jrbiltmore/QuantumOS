import hashlib
import os
import sys

# Path to the file where user credentials are stored
CREDENTIALS_FILE = "user_credentials.txt"

# Ensure the credentials file exists
if not os.path.exists(CREDENTIALS_FILE):
    open(CREDENTIALS_FILE, 'w').close()

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    """Register a new user with a username and password."""
    with open(CREDENTIALS_FILE, 'r') as file:
        for line in file:
            stored_username, _ = line.split(',')
            if stored_username == username:
                print("Username already exists.")
                return False
    with open(CREDENTIALS_FILE, 'a') as file:
        file.write(f"{username},{hash_password(password)}\n")
    print("User registered successfully.")
    return True

def login(username, password):
    """Login a user with a username and password."""
    with open(CREDENTIALS_FILE, 'r') as file:
        for line in file:
            stored_username, stored_password_hash = line.strip().split(',')
            if stored_username == username and stored_password_hash == hash_password(password):
                print("Login successful.")
                return True
    print("Invalid username or password.")
    return False

def main():
    if len(sys.argv) < 4:
        print("Usage: python login_manager.py <action> <username> <password>")
        print("Actions: register, login")
        return
    
    action, username, password = sys.argv[1], sys.argv[2], sys.argv[3]

    if action == "register":
        register(username, password)
    elif action == "login":
        login(username, password)
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
