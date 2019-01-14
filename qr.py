import pyqrcode
from hashlib import md5
from os import system, name  # noqa

if name == 'posix':
    limpar = 'clear'
else:
    limpar = 'cls'
system(limpar)


def qrcode(hash, name):
    q = pyqrcode.create(hash)
    q.png(name, scale=6)
    print('QrCode Generated....')


txt = input('Enter your text: ')
name = input('Enter name for file.png: ')
option = input('do you want to encrypt the message? [y/n]: ').upper()

if name[-4:] != '.png':
    name += '.png'

if option == 'Y':
    hash = md5(txt.encode()).hexdigest()
    qrcode(hash, name)
elif option == 'N':
    qrcode(txt, name)
else:
    print('Invalid option.')
