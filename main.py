from re import search
from main import Flask, render_template, request

app = Flask("web")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.arg.get('word')
    return render_template("report.html",searchingBy=word, potato="sexy")

app.run(host="0.0.0.0")