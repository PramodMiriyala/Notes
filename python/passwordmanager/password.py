"""__GeneratePassword"""
import random
import string
def generate_password(length=12, include_digits=True, include_special_characters=True, 
                       min_upper=1, min_lower=1, min_digit=1, min_special_characters=1):
    """Progarmme generates passwords

    Args:
        length (int, optional): desired length of the password. Defaults to 12.
        include_digits (bool, optional): if user want digits tobe included. Defaults to True.
        include_special_characters (bool, optional): if user want special characters tobe included. Defaults to True.
        min_upper (int, optional): minimum digits . Defaults to 1.
        min_lower (int, optional): minimum lowercase letters. Defaults to 1.
        min_digit (int, optional): minimum digits. Defaults to 1.
        min_special_characters (int, optional): minimum special characters. Defaults to 1.

    Returns:
        str: Generated Password
    """
    password = ""
    total_characters = string.ascii_letters
    for _ in range(min_upper):
        password += random.choice(string.ascii_uppercase)
    for _ in range(min_lower):
        password += random.choice(string.ascii_lowercase)
    if include_digits:
        total_characters += string.digits
        for _ in range(min_digit):
            password += random.choice(string.digits)
    if include_special_characters:
        total_characters += string.punctuation
        for _ in range(min_special_characters):
            password += random.choice(string.punctuation)
    for _ in range(length - len(password)):
        password += random.choice(total_characters)
    return password

