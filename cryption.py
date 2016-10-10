import httplib
import base64
import math
import Crypto.Cipher.AES
import zlib


def encrypt(key, plaintext):

    """
    Encrypt the input string
    """
    compresslevel = 9
    compress = zlib.compressobj(compresslevel, zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL, 0)
    nvpstring = compress.compress(this_string)
    nvpstring = compress.flush()

    # encrypt compressed nvpstring
    enc_key = "09KzF2qMBy58ZWg137N$I4h6UwJvp!ij"  # used as an example, contact Vanco for your unique encryption key
    cryptoobj = Crypto.Cipher.AES.new(key)
    encryptednvp = base64.urlsafe_b64encode(
        cryptoobj.encrypt(nvpstring.ljust(int(math.ceil(len(nvpstring) / 16.0) * 16))))

    return encryptednvp


def decrypt(key, text):
    cipher = Crypto.Cipher.AES.new(key)
    return cipher.decrypt(base64.urlsafe_b64decode(text))