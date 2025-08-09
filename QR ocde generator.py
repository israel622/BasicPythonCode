import qrcode

def generte_code(text):

    qrcode1 = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qrcode1.add_data(text)
    qrcode1.make(fit=True)
    image = qrcode1.make_image(fill="black", back_color="white")
    image.save('israelqrcode.png')

url = input('Enter a URL here: ')
generte_code(url)
generte_code('I love you')