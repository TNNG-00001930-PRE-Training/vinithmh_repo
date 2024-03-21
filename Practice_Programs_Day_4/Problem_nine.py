import re

def is_valid_password(password):
    # Define regular expressions for each criteria
    regex_list = [
        r"[a-z]",  # At least 1 lowercase letter
        r"[A-Z]",  # At least 1 uppercase letter
        r"[0-9]",  # At least 1 digit
        r"[$#@]",  # At least 1 character from [$#@]
        r".{6,12}"  # Password length between 6 and 12 characters
    ]

    # Check if password satisfies all criteria
    for regex in regex_list:
        if not re.search(regex, password):
            return False

    return True

# Example usage
passwords = input("Enter comma separated passwords: ").split(',')
valid_passwords = [password for password in passwords if is_valid_password(password)]
print(','.join(valid_passwords))
