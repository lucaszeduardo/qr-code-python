from PIL import Image
from pyzbar.pyzbar import decode

name = input('Enter name file.png: ')

data = str(decode(Image.open(name))[0][0])

if input('This file is cript? [y/n]: ').upper() == 'Y':
    response = data.replace("'", '')[1:]
else:
    response = data.replace('b', '').replace('\'', '')
print(response)
