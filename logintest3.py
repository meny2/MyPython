import tkinter as tk
from tkinter import messagebox
from check_user_login import check_user_login

def login():
    username = username_entry.get()
    password = password_entry.get()
    check_user_login(username, password)
'''
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        # Add code here to proceed after successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
'''

# Create main window
root = tk.Tk()
root.title("Login")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
