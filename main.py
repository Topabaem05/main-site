from flask import Flask, render_template, request

app = Flask("Flask")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get("word")

    return render_template(
      "templates/report.html",
      searchingBy = word
    )

app.run(host="0.0.0.0")