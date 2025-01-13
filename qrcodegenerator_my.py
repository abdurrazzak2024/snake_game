import qrcode
import image
qr = qrcode.QRCode(
    version = 20,
    box_size = 20,
    border = 20,

)

data = "https://github.com/abdurrazzak23"


qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fiLL="black",back_color = "white")
img.save("test.png")