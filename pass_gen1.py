import secrets
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Collect user preferences
length = int(input("Enter the password length: "))
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

# Generate and display the password
password = generate_password(length, use_uppercase, use_digits, use_special)
print(f"Generated password: {password}")
