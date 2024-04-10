import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                  (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

# Function to add item to inventory
def add_item(name, quantity):
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    print(f"{name} added to inventory with quantity: {quantity}")

# Function to remove item from inventory
def remove_item(name):
    cursor.execute("DELETE FROM inventory WHERE name=?", (name,))
    conn.commit()
    print(f"{name} removed from inventory")

# Function to update item quantity
def update_quantity(name, new_quantity):
    cursor.execute("UPDATE inventory SET quantity=? WHERE name=?", (new_quantity, name))
    conn.commit()
    print(f"Quantity for {name} updated to {new_quantity}")

# Function to view current inventory
def view_inventory():
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    if not inventory:
        print("Inventory is empty")
    else:
        print("Current Inventory:")
        for item in inventory:
            print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}")

# Function to search for items by name
def search_item(name):
    cursor.execute("SELECT * FROM inventory WHERE name=?", (name,))
    item = cursor.fetchone()
    if item:
        print(f"Name: {item[1]}, Quantity: {item[2]}")
    else:
        print("Item not found")

# Main function
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. View Inventory")
        print("5. Search Item")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            add_item(name, quantity)
        elif choice == '2':
            name = input("Enter item name to remove: ")
            remove_item(name)
        elif choice == '3':
            name = input("Enter item name to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            update_quantity(name, new_quantity)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            name = input("Enter item name to search: ")
            search_item(name)
        elif choice == '6':
            print("Exiting program")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
