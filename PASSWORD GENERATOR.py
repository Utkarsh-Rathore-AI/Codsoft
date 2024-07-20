import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    characters = lower
    if include_uppercase:
        characters += upper
    if include_numbers:
        characters += numbers
    if include_special_chars:
        characters += special_chars

    password = []
    if include_uppercase:
        password.append(random.choice(upper))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_special_chars:
        password.append(random.choice(special_chars))
    
    password += random.choices(characters, k=length-len(password))
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()