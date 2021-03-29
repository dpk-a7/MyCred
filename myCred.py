import os
import argparse
import sys
from cryptography.fernet import Fernet

with open('do_not_delete.key') as filekey:
	key = filekey.read()
_fernet = Fernet(key)

def encryptor_(foldername):
	all_file = []
	os.chdir(f'./{foldername}')
	for i in os.listdir():
		all_file.append(str(i))
	for j in all_file:
		with open(j, 'rb') as file:
			original = file.read()
		encrypted = _fernet.encrypt(original)
		with open(j, 'wb') as encrfile:
			encrfile.write(encrypted)
	os.chdir(f'..')
	print("Encryption done successfully!")
def decryptor_(foldername):
	all_file = []
	os.chdir(f'./{foldername}')
	for i in os.listdir():
		all_file.append(str(i))
	for j in all_file:
		with open(j, 'rb') as file:
			original = file.read()
		encrypted = _fernet.decrypt(original)
		with open(j, 'wb') as encrfile:
			encrfile.write(encrypted)
	print("Decryption done successfully!")


def fld(name : str)-> "Name of the folder":
	if name.m:
		try:
			if name.m in os.listdir():
				print("folder already exist!")
			else:
				os.system(f"mkdir {name.m}")
				print(f"{name.m} made successfully!")
		except Exception:
			print("Error Occured while executing the command!")
	elif name.r:
		try:
			if name.r in os.listdir():
				os.system(f"rmdir \s {name.r}")
				print(f"{name.r} successfully removed!")
			else:
				print("folder not found!")
		except Exception:
			print("Error Occured while executing the command!")
	elif name.hd:
		try:
			if name.hd in os.listdir():
				encryptor_(name.hd)
				os.system(f"Attrib +h +s +r {name.hd}")
				print(f"{name.hd} hide successful!")
			else:
				print("folder not found!")
		except Exception:
			print("Error Occured while executing the command!")
	elif name.uh:
		try:
			if name.uh in os.listdir():
				os.system(f"Attrib -h -s -r {name.uh}")
				decryptor_(name.uh)
				print(f"{name.uh} unhide successful!")
			else:
				print("folder not found!")
		except Exception:
			print("Error Occured while executing the command")
	elif name.ls == "this":
		for i in os.listdir():
			print(i)
	elif name.ls:
		for i in os.listdir(f"{name.ls}"):
			print(i)
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', type = str,help = "Enter name to make folder")
	parser.add_argument('-r', type = str,help = "Enter name to remove folder")
	parser.add_argument('-hd', type = str,help = "Enter name to hide folder")
	parser.add_argument('-uh', type = str,help = "Enter name to unhide folder")
	parser.add_argument('-ls', type = str, help = "List all the items ")
	arg = parser.parse_args()
	fld(arg)
