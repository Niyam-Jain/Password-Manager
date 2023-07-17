# Password Manager

This is a simple command-line password manager that allows you to store, retrieve, and delete passwords for different websites. The passwords are securely encrypted using the AES (Advanced Encryption Standard) algorithm.

## Features

- Add a password: Store a new password for a specific website along with the corresponding username.
- Get a password: Retrieve a password for a given website and copy it to the clipboard.
- Delete a password: Remove a stored password for a website.
- Password Requirements: Passwords must meet the following criteria:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one special character
  - At least one number
  - Minimum length of 8 characters

## Prerequisites

- Python 3.6 or above
- `cryptography` library: Install it by running `pip install cryptography`
- `pyperclip` library: Install it by running `pip install pyperclip`

## Getting Started

1. Clone the repository:


2. Install the required dependencies:


3. Generate the encryption key:


This will create an encryption key file named `encryption.key`. Keep this file secure as it is required to encrypt and decrypt passwords.

4. Run the password manager:


The password manager will display a menu with options to add, retrieve, and delete passwords.

## Usage

1. Add a password:

- Enter the website name.
- Enter the username associated with the website.
- Enter the password. Make sure it meets the specified requirements.

2. Get a password:

- Enter the website name for which you want to retrieve the password.
- The password will be displayed on the screen and copied to the clipboard.

3. Delete a password:

- Enter the website name for which you want to delete the password.
- The password will be removed from the password manager.

4. Quit:

- Select this option to exit the password manager.

## Security Considerations

- Keep the `encryption.key` file secure and do not share it with others. This file contains the encryption key required to encrypt and decrypt passwords.
- Ensure that your system is protected against unauthorized access to prevent others from accessing the password manager and the stored passwords.

## License

This project is licensed under the [MIT License](LICENSE).

