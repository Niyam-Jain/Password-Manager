import json
import getpass
import re
from cryptography.fernet import Fernet
import pyperclip

PASSWORDS_FILE = "passwords.json"
ENCRYPTION_KEY_FILE = "encryption.key"


def generate_encryption_key():
    key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as file:
        file.write(key)


def load_encryption_key():
    with open(ENCRYPTION_KEY_FILE, "rb") as file:
        key = file.read()
    return key


def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password


def load_passwords():
    try:
        with open(PASSWORDS_FILE, "r") as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}
    return passwords


def save_passwords(passwords):
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(passwords, file, indent=4)


def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"
    return re.match(pattern, password) is not None


def add_password(passwords, website, username, password, key):
    if website in passwords:
        print("A password for that website already exists.")
    elif not is_valid_password(password):
        print("Password does not meet the requirements.")
        print("Please ensure it contains at least one uppercase letter, one lowercase letter, "
              "one special character, one number, and is at least 8 characters long.")
    else:
        encrypted_password = encrypt_password(password, key)
        passwords[website] = {"username": username, "password": encrypted_password.decode()}
        save_passwords(passwords)
        print(f"Password for {website} added successfully.")


def get_password(passwords, website, key):
    if website in passwords:
        password_data = passwords[website]
        decrypted_password = decrypt_password(password_data['password'].encode(), key)
        pyperclip.copy(decrypted_password)  # Copy password to clipboard
        print(f"Website: {website}")
        print(f"Username: {password_data['username']}")
        print("Password has been copied to the clipboard.")
    else:
        print("No password found for that website.")


def delete_password(passwords, website):
    if website in passwords:
        del passwords[website]
        save_passwords(passwords)
        print(f"Password for {website} deleted successfully.")
    else:
        print("No password found for that website.")


def main():
    try:
        key = load_encryption_key()
    except FileNotFoundError:
        print("Encryption key not found. Generating a new key...")
        generate_encryption_key()
        key = load_encryption_key()

    passwords = load_passwords()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add a password")
        print("2. Get a password")
        print("3. Delete a password")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            add_password(passwords, website, username, password, key)
        elif choice == "2":
            website = input("Enter website: ")
            get_password(passwords, website, key)
        elif choice == "3":
            website = input("Enter website: ")
            delete_password(passwords, website)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
