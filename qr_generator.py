import qrcode

def generar_qr(texto):
    qr = qrcode.make(texto)
    qr.save("qr.png")

texto = input("Texto: ")
generar_qr(texto)