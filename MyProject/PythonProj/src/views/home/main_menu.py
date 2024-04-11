import tkinter as tk

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")  # Set window size to cover entire monitor

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.mainloop()



