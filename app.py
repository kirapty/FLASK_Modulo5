from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/discord')
def discord():
    return render_template("discord.html")

@app.route('/whatsapp')
def whatsapp():
    return render_template("whatsapp.html")

@app.route('/slang')
def slang():
    return render_template("slang.html")