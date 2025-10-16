import qrcode

# Get input from user
data = input("Enter text or URL: ").strip()

# Create the QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,  # Small box for terminal display
    border=2
)
qr.add_data(data)
qr.make(fit=True)

# Print the QR code in ASCII
qr.print_ascii(invert=True)  # invert=True makes the blocks blacki
