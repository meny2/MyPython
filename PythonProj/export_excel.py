#pip install openpyxl
import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

def generate_excel():
    # สร้าง Workbook
    wb = Workbook()
    ws = wb.active

    # เพิ่มข้อมูลตัวอย่าง
    data = [
        ['Header 1', 'Header 2', 'Header 3'],
        ['Data 1', 'Data 2', 'Data 3'],
        ['Data 4', 'Data 5', 'Data 6']
    ]

    # ใส่ข้อมูลลงใน Worksheet
    for row in data:
        ws.append(row)

    # บันทึกไฟล์ Excel
    file_path = 'static/exportfile/output.xlsx'
    wb.save(file_path)

    messagebox.showinfo("สร้าง Excel", "ไฟล์ Excel ได้ถูกสร้างเรียบร้อยแล้วที่ {}".format(file_path))

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Export Excel")

# สร้างปุ่มสำหรับสร้าง Excel
generate_excel_button = tk.Button(root, text="สร้าง Excel", command=generate_excel)
generate_excel_button.pack()

root.mainloop()
