## PyCipher.net

* Advanced Encryption Standard (PCI) Level 1 128-bit Encryption Methodology
* Encryption/Encoding (with Flask and PyCrypto)

##### Modules:

* Crypto.Cipher.AES
* base64
* math
* hashlib

##### Usage:

* Compress
* Pad
* Encrypt
* Encode

AES-128 bit encryption with 16 bytes block size and CBC mode:  each block is XORed with the previous ciphertext block before being encrypted.

enckey = 'a very secret key' - must be a valid 16-byte string

payload = 'the string to be encrypted'

_cipher = cipher.AESCipher(enckey)

encrypted_string = _cipher.encrypt(payload)

print('Encrypted String: ' + str(encrypted_string))


