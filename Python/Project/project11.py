# Project 11: Random Password Generator


import random
import string
def generate_password(length=12):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
def main():
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()