"""3.Password Generator
1.The program should prompt the user to specify the desired password length.
2.The user should be able to choose whether to include uppercase letters, lowercase letters, digits, and/or special characters in the generated password.
3.Based on the user's choices, the program should generate a random password that meets the specified criteria.
4.The generated password should be displayed to the user.
5.The program should provide an option to generate a new password or exit."""\


import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Please choose at least one type of character to include in the password.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        print("Password Generator")
        length = int(input("Enter desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        if password:
            print("Generated Password:", password)
        
        choice = input("Generate a new password? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()


