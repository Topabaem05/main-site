from flask import Flask, render_template,request,redirect
from scrapper import get_jobs
app=Flask("SuperScapper")

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/report")
def report():
 word=request.args.get('word')
 if word:
  word=word.lower()
  jobs=get_jobs(word)
 else:
   return redirect("/") 
 return render_template("report.html")

app.run(host="120.0.0.7") 