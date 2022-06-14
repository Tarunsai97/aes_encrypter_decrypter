from flask import Flask, render_template
from requests import request

app = Flask("__name__")


@app.route("/")
def home():
    return render_template('base.html')


@app.route("/encrypt")
def encrypt():
    if request.method == "POST":
        password = request.form.get()
    return render_template('encrypton.html')


@app.route("/decrypt")
def decrypt():
    return render_template('decrypton.html')
