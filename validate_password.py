def is_password_safe(password):
    # Condition 1: Minimum 8 characters
    if len(password) < 8:
        return False

    # Condition 2: Alphabets between [a-z]
    if not any(char.islower() for char in password):
        return False

    # Condition 3: At least one alphabet should be uppercase [A-Z]
    if not any(char.isupper() for char in password):
        return False

    # Condition 4: At least one digit between [0-9]
    if not any(char.isdigit() for char in password):
        return False

    # Condition 5: At least one symbol like [_ or @ or $]
    symbols = ['_', '@', '$']
    if not any(char in symbols for char in password):
        return False

    return True

# Input password
password = input("Enter your password: ")

# Check if password is safe
if is_password_safe(password):
    print("Your password is safe.")
else:
    print("Your password does not meet the safety requirements.")
