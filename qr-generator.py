import qrcode

# Data to encode
data = "xxx" 

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # 1 to 40 (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qrcode.png")

print("QR Code generated and saved as my_qrcode.png")
