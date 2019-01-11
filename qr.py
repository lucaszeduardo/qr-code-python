import pyqrcode
import hashlib
from os import system

system('clear')

def Md5(text):
	hash_ = hashlib.md5(f'{text}'.encode()).hexdigest()

	return hash_

def QrCode(hash_, name):
	q = pyqrcode.create(hash_)
	q.png(name, scale=6)
	print('QrCode Generated....')

txt = input('Enter Your Text: ')
name = input('Enter Name for file.png: ')
opc = input('do you want to encrypt the message? [y/n]: ').upper()

if tuple(name[:-4]) != '.png':
	name = name + '.png'

if opc == 'Y':
	hash_ = Md5(txt)
	QrCode(hash_, name)
elif opc == 'N':
	QrCode(txt, name)
else:
	print('Opc Invalid....')
