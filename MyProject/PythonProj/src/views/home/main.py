import tkinter as tk
from main_menu import MainMenu  # Import the MainMenu class

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Page")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")  # Set window size to cover entire monitor
        
        # Username entry
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        
        # Password entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        # Login button
        self.login_button = tk.Button(self, text="Login", command=self.open_login)
        self.login_button.pack(pady=10)
    
    def open_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "password":
            self.destroy()
            main_menu = MainMenu()
            main_menu.mainloop()
        else:
            error_label = tk.Label(self, text="Invalid username or password", fg="red")
            error_label.pack(pady=5)

if __name__ == "__main__":
    main_page = MainPage()
    main_page.mainloop()
