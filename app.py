from flask import Flask, flash, render_template, url_for, request, redirect
from datetime import datetime
import config
import cryption
import base64
import math
import Crypto.Cipher.AES
import zlib

app = Flask(__name__)
app.enc_key = config.ENCRYPT_KEY
app.secret_key = config.SECRET_KEY
app.url_map.strict_slashes = False
app.DEBUG = config.DEBUG


@app.route('/', methods=['GET', 'POST'])
def index():
    message = 'Welcome to encrypted.me.  Please enter your string to encrypt or decrypt'
    encryptednvp = None

    return render_template(
        'index.html',
        message=message
    )

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    Encrypt function
    """
    if request.method == 'POST':
        nvpstring = request.form['enc_val']

        if len(nvpstring) != 0:
            try:
                cryption.encrypt(enc_key, plaintext=nvpstring)
            except (ValueError, TypeError) as e:
                return 'Sorry, an error has occurred' + str(e)
        else:
            encryptednvp = None
            flash('Can not encrypt an empty string.  Please try again...')


    return render_template(
        'encrypt.html',
        encryptednvp=encryptednvp
    )


@app.route('/decrypt', methods=['POST'])
def decrypt():
    """
    Decrypt function
    """
    if request.method == 'POST':
        nvpstring = request.form['enc_val']

        if len(nvpstring) != 0:
            try:
                cryption.decrypt(enc_key, text=nvpstring)
            except (ValueError, TypeError) as e:
                return 'Sorry, an error has occurred' + str(e)
        else:
            encryptednvp = None
            flash('Can not decrypt an empty string.  Please try again...')


    return render_template(
        'decrypt.html',
        encryptednvp=decryptednvp
    )


if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=5555,
        debug=app.DEBUG,
    )



