import des
import sys
from RSA import generate_keypair, encrypt, decrypt
import struct

# Defining some important variables
SIZE = 1024
des_key = '1'
path = "penguin.jpg"

p = 1297273  # Get your P value from the excel file
q = 1297651  # Get your P value from the excel file

# Part 1 - Generate the public, private keypair
public, private = generate_keypair(p, q)
print("RSA Public Key pair = " + str(public))
print("RSA Private Key pair = " + str(private))

# Input DES key (8 characters long)
while len(des_key) != 8:
    des_key = input("Enter the DES key, 8 Characters")
    if len(des_key) != 8: print("wrong! 8 characters. Try again:")

# Part 2 - Encrypt the DES key
print("Encrypting DES KEY with RSA...")
des_encoded = [str(encrypt(public, chars)) for chars in des_key]
print("the encrypted key is " + str(des_encoded))

# Encrypt the image with DES
print('Encrypting image using DES')
file = open(path, "rb")
image_data = file.read()
file.close()
coder = des.des()
r = coder.encrypt(des_key, image_data, cbc=False)  # encrypted image

# Write the encrypted image into file
r_byte = bytearray()
for x in r:
    r_byte += bytes([ord(x)])
file = open(r'penguin_encrypted.bin', "wb+")
file.write(r_byte)
file.close()

# Recover DES Key
des_key_decoded = []
for data in des_encoded:
    cipher = int(data)
    des_key_decoded += decrypt(private, cipher)
print("DES key decoded = " + str(des_key_decoded))
print("Decrypting the image with the recovered key")
decoder = des.des()
des_key_decoded_str = ''
for i in des_key_decoded:
    des_key_decoded_str = des_key_decoded_str + str(i)
rr = decoder.decrypt(des_key, r, cbc=False)  # this is in string  format, must convert to byte format
rr_byte = bytearray()
for x in rr:
    rr_byte += bytes([ord(x)])
# write to file to make sure it is okay
file2 = open(r'penguin_decrypted.jpg', "wb")
file2.write(bytes(rr_byte))
file2.close()
print('decrypting image completed')

# Check for correct encryption/decryption
if bytes(rr_byte) == image_data:
    print('image decoded successfully')
else:
    print('image not decoded correctly')
