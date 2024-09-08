"""__summary__"""
from password import generate_password
from store import store_password, retrive_password

gen_password = generate_password()

store_password("github",'xyz.gmail.com', gen_password)

print(retrive_password("github"))
