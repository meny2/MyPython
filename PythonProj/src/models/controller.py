from models import create_product, read_products, update_product, delete_product
from database import check_login

def login(username, password):
    return check_login(username, password)

def add_product(name, price):
    create_product(name, price)

def view_products():
    return read_products()

def update_existing_product(id, name, price):
    update_product(id, name, price)

def remove_product(id):
    delete_product(id)
