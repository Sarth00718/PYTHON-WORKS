'''Write a Python program to check the validity of passwords input by users'''
def is_valid_password(password):
    
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
        return True
    else:
        return False

user_password = input("Enter a password: ")

if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is not valid. Please ensure it has at least 8 characters, contains both uppercase and lowercase letters, and at least one digit.")