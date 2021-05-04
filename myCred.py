import os
import sys
import pip
import platform

os_type = platform.uname()
opsys = os_type[0]
opnm = os_type[1]
try:
	import argparse
	from cryptography.fernet import Fernet
	from progress.bar import IncrementalBar
except:
	if hasattr(pip, 'main'):
		pip.main(['install',"argparse"])
		pip.main(['install',"cryptography"])
		pip.main(['install', 'progress'])
	else:
		pip._internal.main(['install','argparse'])
		pip._internal.main(['install','cryptography'])
		pip._internal.main(['install', 'progress'])
finally:
	import argparse
	from cryptography.fernet import Fernet
	from progress.bar import IncrementalBar
try:
	with open('do_not_delete.key') as filekey:
		key = filekey.read()
	_fernet = Fernet(key)
except:
	print("do_not_delete.key not found!")

def Generator():
	key = Fernet.generate_key()
	with open('do_not_delete.key', 'wb') as filekey:
		filekey.write(key)
	print(f"\nKey generated: do_not_delete.key \nPath: {os.getcwd()}")

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
				os.system(f"rmdir /s {name.r}")
				if name.r not in [i for i in os.listdir()]:
					print(f"{name.r} successfully removed!")
				else:
					print(f"{name.r}-> Remove operation cancelled!")
			else:
				print(f"{name.r} not found!")
		except Exception:
			print("Error Occured while executing the command!")
	elif name.g == 'y':
		Generator()
	elif name.hd:
		try:
			if name.hd in os.listdir():
				unchn = []
				bar_ = IncrementalBar(max = len(os.listdir(name.hd)))
				for i in os.listdir(name.hd):
					if os.path.isdir(name.hd+"/"+ i) == True:
						foldername = name.hd+"/"+ i
						os.chdir(f'./{foldername}')
						all_file = os.listdir()
						bar = IncrementalBar(max = len(all_file))
						for i__ in all_file:
							with open(i__, 'rb') as file:
								original = file.read()
							encrypted = _fernet.encrypt(original)
							with open(i__, 'wb') as encrfile:
								encrfile.write(encrypted)
							bar.next()
						for _ in range(2):
							os.chdir('..')

					elif os.path.isdir(name.hd+"/"+ i) == False:
						file_name = name.hd+"/"+ i
						with open(file_name, 'rb') as file:
							original = file.read()
						encrypted = _fernet.encrypt(original)
						with open(file_name, 'wb') as encrfile:
							encrfile.write(encrypted)
					else:
						unchn.append(i)
					bar_.next()
				if opsys == "Windows":
					os.system(f"Attrib +h +s +r {name.hd}")
				elif opsys == "Linux":
					os.system(f"mv {name.hd} .{name.hd}")
				print("\n-->Encryption done successfully!")
				print(f"-->Dir: {name.hd} hide successful!")
				X = "File that were unchanged!" if len(unchn) != 0 else ""
				print(X)
				if len(unchn) != 0:
					for i in unchn:
						print(i)
			else:
				print(f"{name.hd} not found!")
		except Exception as e:
			print(f" Error Occured while executing the command!\n\
				* Maybe the {name.hd} is already hidden 'OR'\n\
				* The Files are not Encriptable!\n<Error Message>\n",e)
	elif name.uh:
		try:
			if name.uh in os.listdir():
				unchn = []
				bar_ = IncrementalBar( max = len(os.listdir(name.uh)))
				for i in os.listdir(name.uh):
					if os.path.isdir(name.uh+"/"+ i) == True:
						foldername = name.uh+"/"+ i
						os.chdir(f'./{foldername}')
						all_file = os.listdir()
						bar = IncrementalBar( max = len(all_file))
						for i__ in all_file:
							with open(i__, 'rb') as file:
								original = file.read()
							decrypted = _fernet.decrypt(original)
							with open(i__, 'wb') as decrfile:
								decrfile.write(decrypted)
							bar.next()
						for _ in range(2):
							os.chdir('..')

					elif os.path.isdir(name.uh+"/"+ i) == False:
						file_name = name.uh+"/"+ i
						with open(file_name, 'rb') as file:
							original = file.read()
						decrypted = _fernet.decrypt(original)
						with open(file_name, 'wb') as decrfile:
							decrfile.write(decrypted)
					else:
						unchn.append(i)
					bar_.next()
				if opsys == "Windows":
					os.system(f"Attrib -h -s -r {name.uh}")
				elif opsys == "Linux":
					os.system(f"mv .{name.uh} {name.uh}")
				print("\n-->Decryption done successfully!")
				print(f"-->Dir: {name.uh} unhide successful!")
				X = "File that were unchanged!" if len(unchn) != 0 else ""
				print(X)
				if len(unchn) != 0:
					for i in unchn:
						print(i)
			else:
				print(f"{name.uh} not found!")
		except Exception as e:
			print(f" Error Occured while executing the command!\n\
				* Maybe the {name.uh} is already visible 'OR'\n\
				* The Files are not Decriptable!\n<Error Message>\n",e)
	elif name.ls == "this":
		for i in os.listdir():
			print(i)
	elif name.ls:
		try:
			if os.listdir(f"{name.ls}"):
				for i in os.listdir(f"{name.ls}"):
					print(i)
			else:
				print(f"{name.ls} is empty!")
		except:
			print(f"{name.ls} not found!")
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-g', type = str,help = "Generate 'New Key'---------->[myCred.py -g y]")
	parser.add_argument('-m', type = str,help = "Enter name to make folder--->[myCred.py -m <dir name>]")
	parser.add_argument('-r', type = str,help = "Enter name to remove folder->[myCred.py -r <dir name>]")
	parser.add_argument('-hd', type = str,help = "Enter name to hide folder--->[myCred.py -hd <dir name>]")
	parser.add_argument('-uh', type = str,help = "Enter name to unhide folder->[myCred.py -uh <dir name>]")
	parser.add_argument('-ls', type = str, help = "List all the items---------->[myCred.py -ls this] or [myCred.py -ls <dir name>]")
	arg = parser.parse_args()
	fld(arg)
