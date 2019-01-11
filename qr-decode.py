from PIL import Image
from pyzbar.pyzbar import decode

name = input('Enter name file.png: ')

data = decode(Image.open(name))
data_ = data[0][0]
opc = input('This file is cript? [y/n]: ').upper()

if opc == 'Y':
	rp1 = str(data_).replace("'",'')
	rp2 = list(str(rp1))
	rp3 = rp1[1:]
	rp4 = ''.join(rp3)
	print(rp4)
else:
	rp1 = str(data_).replace('b','')
	rp2 = str(rp1).replace("'", '')
	print(rp2)
