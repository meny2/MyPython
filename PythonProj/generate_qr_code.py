import os
import qrcode

def generate_qr_code_for_product(product_data, file_path):
    # สร้าง QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(product_data)
    qr.make(fit=True)

    # สร้าง QR code ในรูปแบบภาพ
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # ตรวจสอบว่า path สำหรับเก็บไฟล์มีอยู่หรือไม่ ถ้าไม่มีให้สร้าง directory
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    # บันทึก QR code ลงในไฟล์
    qr_img.save(file_path)

# เรียกใช้งานฟังก์ชัน generate_qr_code_for_product
product_data = "ข้อมูลสินค้า"
file_path = "static/images/product/product_qr_code.png"
generate_qr_code_for_product(product_data, file_path)
