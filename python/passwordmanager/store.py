
PASSWORD_FILE = "password.txt"

def store_password(service_name, user_name, password):
    """this function stores password

    Args:
        service_name (_type_): service_name
        password (str): the password that to be stored
    """
    with open(PASSWORD_FILE, mode="a", encoding="utf-8") as file:
        file.write(f"{service_name}\t{user_name}\t{password}\n")


def retrieve_password(service_name):
    """retrieve password from password file

    Args:
        service_name (str): service_name
    """
    with open(PASSWORD_FILE, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            (service, username, password) = line.split("\t")
            if service == service_name:
                return (username, password)
