import tkinter as tk
from tkinter import messagebox
import random

# Simulated database of user credentials
users = {
    "admin": "password",
    "user1": "123456"
}

def send_reset_email(username):
    # Simulated email sending
    # In a real application, this would send an email to the user's registered email address with a password reset link
    reset_code = random.randint(1000, 9999)
    messagebox.showinfo("Password Reset", f"An email with a reset code has been sent to {username}. The reset code is: {reset_code}")

def reset_password():
    username = username_entry.get()
    if username in users:
        send_reset_email(username)
    else:
        messagebox.showerror("User Not Found", "No user with that username found.")

# Create main window
root = tk.Tk()
root.title("Forget Password")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create reset button
reset_button = tk.Button(root, text="Reset Password", command=reset_password)
reset_button.pack()

# Run the main event loop
root.mainloop()
