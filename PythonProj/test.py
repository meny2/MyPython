import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # ตรวจสอบการเข้าสู่ระบบ
    if username == "admin" and password == "password":
        print("เข้าสู่ระบบสำเร็จ")
    else:
        print("เข้าสู่ระบบล้มเหลว")

def register():
    # สร้างหน้าต่างสำหรับการลงทะเบียน
    register_window = tk.Toplevel(root)
    register_window.title("ลงทะเบียน")

    # สร้างป้ายชื่อและช่องใส่ข้อมูลสำหรับการลงทะเบียน
    new_username_label = tk.Label(register_window, text="ชื่อผู้ใช้:")
    new_username_label.grid(row=0, column=0)
    new_username_entry = tk.Entry(register_window)
    new_username_entry.grid(row=0, column=1)

    new_password_label = tk.Label(register_window, text="รหัสผ่าน:")
    new_password_label.grid(row=1, column=0)
    new_password_entry = tk.Entry(register_window, show="*")
    new_password_entry.grid(row=1, column=1)

    def add_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        # บันทึกข้อมูลผู้ใช้ใหม่ (ในตัวอย่างนี้จะแสดงเฉพาะการพิมพ์เท่านั้น)
        print("เพิ่มผู้ใช้ใหม่:", new_username, new_password)
        register_window.destroy()

    register_button = tk.Button(register_window, text="ลงทะเบียน", command=add_user)
    register_button.grid(row=2, columnspan=2, pady=10)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("เข้าสู่ระบบ")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

username_label = tk.Label(frame, text="ชื่อผู้ใช้:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(frame, text="รหัสผ่าน:")
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(frame, text="เข้าสู่ระบบ", command=login)
login_button.grid(row=2, columnspan=2, pady=5)

register_label = tk.Label(frame, text="Don't have an account? Register here", fg="blue", cursor="hand2")
register_label.grid(row=3, columnspan=2, pady=5)
register_label.bind("<Button-1>", lambda e: register())

root.mainloop()
