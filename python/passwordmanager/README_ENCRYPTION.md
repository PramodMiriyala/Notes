# Encryption

## encoding and decoding file in python

### creating virtual env and installing dependences

```bash
python .\pmanager.py generate -s github -d -c -l 16
python -m venv .venv
pip install cryptography
pip freeze > requirements.txt
from cryptography.fernet import Fernet
```

* Encryption can be of two types
  * Assymetric (same key at both ends - encryption and decryption)
  * symmetric (Two keys - public and private keys)

### Generating the Key

```python
def write_key(key_file = "passwords.key"):
    """this method generates key

    Args:
        key_file (str, optional): file contain keys. Defaults to "passwords.key".
    """
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
```

* `key_file = "passwords.key"` ==> path where key will be stored
* `if not os.path.exists(key_file)` ==> checks weather or not the file exits in the path to write key if won't creates file
* The Fernet.generate_key() function generates a fresh fernet key
* you really need to keep this in a safe place. If you lose the key, you will no longer be able to decrypt data that was encrypted with this key.

### loading generated key for encryption and decryption

```python
def load_key(key_file = "passwords.key"):
    """this method loads the key generated
    """
    with open(key_file, "r", encoding="utf-8") as file:
        key = file.read()
    return key
```

* The key is read from the file, but since it is not assigned to any variable, you cannot use it after the function exits.

###  Encryption

```python
def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data
```

* `f = Fernet(key)` ==> initializing the Fernet class with the key, you are creating an object that can be used to encrypt and decrypt data using the specified key.
* `encrypted = f.encrypt(data)`  ==> f.encrypt() method encrypts the data passed.
* `encode()` ==> The encode() method is used to convert a string (which is in Unicode) into a bytes object. This is necessary when you need to store or transmit text data in a binary format.
  * to encrypt data it must be in binary format, Use `encode()` function to convert data `str --> bytes`


### Decryption

```python
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data)
    return decrypted.decode()
```

* `decode()` method is used to convert a bytes object back into a string.
  * it is nessary to convert data back to str to save to file (or) to read from file

```python
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

```

