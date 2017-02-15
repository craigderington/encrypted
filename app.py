from flask import Flask, flash, render_template, url_for, request, redirect
from datetime import datetime
import config
import cipher

# app settings
app = Flask(__name__)
app.enc_key = config.ENCRYPT_KEY
app.secret_key = config.SECRET_KEY
app.url_map.strict_slashes = False
app.DEBUG = config.DEBUG


@app.route('/', methods=['GET', 'POST'])
def index():
    message = 'Welcome to pycipher.net.  Please enter your string to encrypt!'

    return render_template(
        'index.html',
        message=message
    )


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    Encrypt function
    """
    encrypted_string = None

    if request.method == 'POST':
        payload = request.form['enc_val'].strip()

        if len(payload) != 0:
            try:
                _cipher = cipher.AESCipher(app.enc_key)
                encrypted_string = _cipher.encrypt(payload)
            except (ValueError, TypeError) as e:
                return 'Sorry, an error has occurred ' + str(e)

        else:
            encrypted_string = None
            flash('Can not encrypt an empty string.  Please try again...')

    return render_template(
        'encrypt.html',
        encrypted_string=encrypted_string
    )


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    """
    Decrypt function
    """
    decrypted_string = None

    if request.method == 'POST':
        payload = request.form['enc_val'].strip()

        if len(payload) != 0:
            if len(payload) % 2 == 0:
                try:
                    _cipher = cipher.AESCipher(app.enc_key)
                    decrypted_string = _cipher.decrypt(payload)
                except (ValueError, TypeError) as e:
                    return 'Sorry, an error has occurred ' + str(e)
            else:
                decrypted_string = None
                flash('The input string must be a multiple of 16 in order to decrypt. \
                       Please check your input and try again.')

        else:
            decrypted_string = None
            flash('Sorry, can not decrypt an empty string.  Please check your input and try again...')

    return render_template(
        'decrypt.html',
        decrypted_string=decrypted_string
    )


@app.route('/aes', methods=['GET'])
def aes():
    return render_template(
        'aes.html'
    )


@app.route('/about', methods=['GET'])
def about():
    return render_template(
        'about.html'
    )


@app.route('/docs', methods=['GET'])
def docs():
    return render_template(
        'docs.html'
    )


@app.route('/tos', methods=['GET'])
def tos():
    return render_template(
        'tos.html'
    )


@app.errorhandler(404)
def page_not_found(e):
    render_template(
        '404.html'
    ), 404


@app.errorhandler(500)
def server_error(e):
    render_template(
        '500.html'
    ), 500


if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=config.PORT,
        debug=app.DEBUG,
    )



