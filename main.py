from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template('base.html')


@app.route("/encrypt")
def encrypt():
    return render_template('encrypton.html')


@app.route("/decrypt")
def decrypt():
    return render_template('decrypton.html')
