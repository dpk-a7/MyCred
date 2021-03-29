#import the module
from cryptography.fernet import Fernet

#generate a key and store it as key object
key = Fernet.generate_key()

#save the key to the file 
with open('do_not_delete.key', 'wb') as filekey:
	filekey.write(key)
print("Key generated successfully\nName: do_not_delete.key\nPlease do not delete this file after encrypting the folder!")