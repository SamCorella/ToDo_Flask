from flask import Flask, render_template

app = Flask(__name__)
tasks = []

@app.route("/")
def todo():
    return render_template("index.html")