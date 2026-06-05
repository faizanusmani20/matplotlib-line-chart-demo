            # 1st Version

import qrcode

data=input("Enter the text or Url: ")
filename=input("Enter file name: ")

qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image=qr.make_image(fill_color='black',back_color='white')
image.save(filename)

print(f"File saved as {filename}")

            # 2nd Version

# import qrcode

# data = input("Enter the text or URL: ")
# filename = input("Enter file name (e.g., qr.png): ")

# qr = qrcode.QRCode(
#     box_size=10,
#     border=4
# )

# qr.add_data(data)
# qr.make(fit=True)

# image = qr.make_image(fill_color="black", back_color="white")
# image.save(filename)

# print(f"File saved as {filename}")