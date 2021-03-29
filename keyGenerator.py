from cryptography.fernet import Fernet

key = Fernet.generate_key()
 
with open('do_not_delete.key', 'wb') as filekey:
	filekey.write(key)
print("Key generated successfully\nName: do_not_delete.key\nPlease do not delete this file after encrypting the folder!")
