from flask import Flask, render_template

app = Flask("Flask")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    return "This is the report"


app.run(host="0.0.0.0")