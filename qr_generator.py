import qrcode

def generar_qr(url):
    qr = qrcode.make(url)
    qr.save(f"{nombre}.png")

url = input("Indica la URL de destino --> ")
nombre = input("Indica el nombre del QR --> ")
generar_qr(url)
