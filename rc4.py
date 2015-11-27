'''
Copyright (c) 2015 Manpreet Bahl

This file containts the RC4 implementation
for encrypting and decryption data. The 
implementation follows the Pseudocode given
by Bart Massey. 
'''

#Import Library
import os

#Variables
IV_Size = 10
Array_Size = 256

#RC4 Key Scheduling
def RC4(keystream_len,rounds,key):
	#Length of Key
	key_len = len(key)

	#Initialize the Array
	S = []
	for i in range(Array_Size):
		S.append(i)

	#Key Scheduling
	j = 0
	for k in range(rounds):
		for m in range(Array_Size):
			j = (j+ S[m] + key[m % key_len]) % Array_Size
			temp = S[m]
			S[m] = S[j]
			S[j] = temp

	#Produce Key Stream
	keystream = []
	for var in range(keystream_len):
		keystream.append(var)
	
	j = 0
	for z in range (keystream_len):
		z_not = (z+1) % Array_Size
		j = (j + S[z_not]) % Array_Size
		temp = S[z_not]
		S[z_not] = S[j]
		S[j] = temp
		keystream[z] = S[(S[z_not] + S[j]) % Array_Size]

	return keystream

#Encrypt
def encrypt(message,rounds,key):
	size = len(message)
	iv = bytearray(os.urandom(IV_Size))
	key_not = bytearray(key) + iv

	keystream = RC4(size,rounds,key_not)

	ciphertext = []
	for i in range(size + IV_Size):
		ciphertext.append(i)

	for j in range(IV_Size):
		ciphertext[j] = chr(iv[j])
	
	for k in range(size):
		ciphertext[k+IV_Size] = chr(ord(message[k]) ^ keystream[k])

	return "".join(ciphertext)

#Decrypt
def decrypt(message,rounds,key):
	size = len(message)
	iv = message[:IV_Size]

	message = message[IV_Size:]
	key_not = bytearray(key) + bytearray(iv)

	keystream = RC4(size-IV_Size,rounds,key_not)
	plaintext = []
	for i in range(size-IV_Size):
		plaintext.append(i)

	for j in range(size-IV_Size):
		plaintext[j] = chr(ord(message[j]) ^ keystream[j])

	return "".join(plaintext)	
