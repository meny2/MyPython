#pip install reportlab
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf():
    # สร้างข้อมูลตัวอย่าง
    data = [
        ['Header 1', 'Header 2', 'Header 3'],
        ['Data 1', 'Data 2', 'Data 3'],
        ['Data 4', 'Data 5', 'Data 6']
    ]

    # สร้างไฟล์ PDF
    file_path = 'static/exportfile/output.pdf'
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    table_data = []
    for row in data:
        table_data.append(row)

    # สร้างตาราง
    table = Table(table_data)

    # ปรับแต่งสไตล์ตาราง
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    # เพิ่มตารางเข้าไปในเอกสาร PDF
    doc.build([table])

    messagebox.showinfo("สร้าง PDF", "ไฟล์ PDF ได้ถูกสร้างเรียบร้อยแล้วที่ {}".format(file_path))

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Export PDF")

# สร้างปุ่มสำหรับสร้าง PDF
generate_pdf_button = tk.Button(root, text="สร้าง PDF", command=generate_pdf)
generate_pdf_button.pack()

root.mainloop()
