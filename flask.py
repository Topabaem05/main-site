from flask import Flask, render_template, request

app = Flask("web")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return f"You are looking for a job in {word}"

app.run(host="0.0.0.0")