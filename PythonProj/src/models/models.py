import psycopg2
from database import connect_to_database

def create_product(name, price):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
            connection.commit()
            print("Product created successfully!")
        except psycopg2.Error as e:
            print("Error creating product:", e)
        finally:
            cursor.close()
            connection.close()

def read_products():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return products
        except psycopg2.Error as e:
            print("Error reading products:", e)
            return []
        finally:
            cursor.close()
            connection.close()

def update_product(id, name, price):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE products SET name = %s, price = %s WHERE id = %s", (name, price, id))
            connection.commit()
            print("Product updated successfully!")
        except psycopg2.Error as e:
            print("Error updating product:", e)
        finally:
            cursor.close()
            connection.close()

def delete_product(id):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (id,))
            connection.commit()
            print("Product deleted successfully!")
        except psycopg2.Error as e:
            print("Error deleting product:", e)
        finally:
            cursor.close()
            connection.close()
