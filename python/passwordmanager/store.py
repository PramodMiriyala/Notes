"""read, write, encrypt and decrypt files in python"""
import os
from cryptography.fernet import Fernet

PASSWORD_FILE = "password.txt"

def write_key(key_file = "passwords.key"):
    """this method generates key

    Args:
        key_file (str, optional): file contain keys. Defaults to "passwords.key".
    """
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
            return key

def load_key(key_file = "passwords.key"):
    """this method loads the key generated
    """
    with open(key_file, "r", encoding="utf-8") as file:
        key = file.read()
    return key

def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data)
    return decrypted.decode()

def store_password(service_name, user_name, password):
    """this function stores password

    Args:
        service_name (_type_): service_name
        password (str): the password that to be stored
    """
    key = load_key()
    encrypted_username = encrypt_data(user_name, key)
    encrypted_password = encrypt_data(password, key)
    with open(PASSWORD_FILE, mode="a", encoding="utf-8") as file:
        file.write(f"{service_name}\t{encrypted_username.decode()}\t{encrypted_password.decode()}")


def retrieve_password(service_name):
    """retrieve password from password file

    Args:
        service_name (str): service_name
    """
    key = load_key()
    with open(PASSWORD_FILE, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            service, username, encrypted_password  = line.split("\t")
            if service == service_name:
                decrypted_username = decrypt_data(username.encode(), key)
                decrypted_password = decrypt_data(encrypted_password.encode() , key)
                return (decrypted_username, decrypted_password)


