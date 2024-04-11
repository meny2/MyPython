import barcode
from barcode import Code128
from barcode.writer import ImageWriter

# Sample barcode value
barcode_value = '123456789012'

# Generate barcode
barcode_instance = Code128(barcode_value)

# Save barcode image with ImageWriter
barcode_instance.save('barcode_image', options={"write_text": False})




'''
import barcode
from barcode import EAN13
from barcode.writer import ImageWriter

# Generate barcode
barcode_class = EAN13('123456789012')
barcode_class.save('barcode_example', options={"write_text": False})



import barcode
from barcode import Code128
from barcode.writer import ImageWriter

# Generate barcode
barcode_class = Code128('123456789012')
barcode_class.save('barcode_example', options={"write_text": False})
'''