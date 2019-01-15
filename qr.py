import pyqrcode
from hashlib import md5
from os import system as sy, name  # noqa
from PIL import Image
from pyzbar.pyzbar import decode

if name == 'posix':
    limpar = 'clear'
else:
    limpar = 'cls'
sy(limpar)


def qrcode(hash, name):
    q = pyqrcode.create(hash)
    q.png(name, scale=6)
    print('QrCode Generated....')


def main():
    create = input('Do you want create or load a qr file [c/l]: ').lower()
    if create == 'c':
        txt = input('Enter your text: ')
        name = input('Enter name for file.png: ')
        option = input('do you want to encrypt the message? [y/n]: ').lower()
        if name[-4:] != '.png':
            name += '.png'
        if option == 'Y':
            hash = md5(txt.encode()).hexdigest()
            qrcode(hash, name)
        elif option == 'N':
            qrcode(txt, name)
        else:
            print('Invalid option.')
    elif create == 'l':
        name = input('Enter name file.png: ')
        data = str(decode(Image.open(name))[0][0])
        if input('This file is cript? [y/n]: ').upper() == 'Y':
            response = data.replace("'", '')[1:]
        else:
            response = data.replace('b', '').replace('\'', '')
        print(response)


if __name__ == '__main__':
    main()
