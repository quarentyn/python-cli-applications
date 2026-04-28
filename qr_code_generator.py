import qrcode

data = input("Enter a valid Url: ").strip()

file_name = input("How do you want to name this file?: ")

file_pathh = f"D:\\001 test\\{file_name}.png"

qr = qrcode.QRCode()
qr.add_data(data)

img = qr.make_image()
img.save(file_pathh)

print(f"Print QR Code Successfully Generated")