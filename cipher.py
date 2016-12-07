#! /usr/bin/python

import base64
import hashlib
import json
from Crypto import Random
from Crypto.Cipher import AES

"""
Cryptography helpers, used for cookie encryption by AES(Rijmen-128) encryption algorithm
"""


class AESCipher:

    def __init__(self, key):
        """
        Initialize encryption key and block size

        We use AES-128 with 16 bytes block size and CBC mode

        Usage:

        cipher = AESCipher('very secret key')
        encrypted_string = cipher.encrypt('This string will be encrypted')
        decrypted_string = cipher.decrypt(encrypted_string)

        >> decrypted_string = 'This string will be encrypted'

        :param key: string
        :return:
        """
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        """
        Encrypt string

        How it works:

        1. Pad string for encryption (string must be a multiple of BLOCK_SIZE in length)
        2. Create random byte string initialization vector to use for encryption or decryption
        3. Encrypt string and add at the beginning initialization vector (initialization vector length == BLOCK_SIZE)
        4. Encode result byte string to base64

        :param raw:
        :return: string base64 decoded
        """

        # Pad string for encryption (string must be a multiple of BLOCK_SIZE in length)
        raw = self._pad(raw)

        # Create random byte string initialization vector to use for encryption and decryption
        iv = Random.new().read(AES.block_size)

        # Create cipher
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Encrypt string and add at the beginning initialization vector (initialization vector length == BLOCK_SIZE)
        # Encode result byte string to base 64
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        """
        Encrypt string

        How it works:

        1. Decode base64 string
        2. Extract from byte string BLOCK_SIZE bytes this will our initialization vector
        3. Decrypt string without initialization vector
        4. Unpad string

        :param enc: base64 decoded string
        :return: string
        """

        # Decode base64 string
        enc = base64.b64decode(enc)

        # Extract from byte string BLOCK_SIZE bytes this will our initialization vector
        iv = enc[:AES.block_size]

        # Decrypt string without initialization vector
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Decrypt string without initialization vector
        # Unpad string
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        """
        Add padding at the and of string (string must be a multiple of BLOCK_SIZE in length)

        :param s:
        :return:
        """
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        """
        Remove padding from string

        :param s:
        :return:
        """
        return s[:-ord(s[len(s)-1:])]

