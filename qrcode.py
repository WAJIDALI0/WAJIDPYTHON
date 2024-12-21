import qrcode

url = 'http://www.Wajid'
qr = qrcode.QRCode()
qr.add_url(url)
qr.make()
img = qr.make_image()
img.save('qrcode.png')
print('qrcode is generated  successfully')
