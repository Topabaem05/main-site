from flask import Flask, render_template,request,redirect,send_file  #render_template: html을 main문으로(유저에게) 이동시켜주기 위해서, request: 사용자가 찾으려는 단어를 찾기 위해서 
from scrapper import get_jobs
from exporter import save_to_file

app=Flask("SuperScapper")#앱 이름 

db={} #DB는 라우트 외부에 나와있어야 함 ,report가 실행될때마다 초기화가 되면 안되니까



@app.route("/")
def home():
  return render_template("home.html")
  #return "Hello! Welcome to mi casa!"


@app.route("/report")
def report():
  word=request.args.get('word') #word 이름의 argument를 request에서 뽑은것 
  if word:
   word=word.lower() #소문자 처리리
   fromDb = db.get(word)
   if fromDb: 
     jobs=fromDb
   else:
    jobs=get_jobs(word)#DB에 단어가 없다면 scrapper를 돌리면 된다.
    db[word]=jobs #scrapping을 마친 jobs를 DB에 넣어주면 됨
  else:
    return redirect("/") 
  return render_template("report.html",searchingBy=word,resultsNumber=len(jobs),jobs=jobs) #report.html로 가는 정보들들
  # 변수들을 {{}}안에 넣어줘서 사용자한테 보여줌


@app.route("/export")
def export():
  try:
    word=request.args.get('word') #word 이름의 argument를 request에서 뽑은것 
    if not word:
      raise Exception() #except 블록으로 가게 만들어줌 
    jobs=db.get(word)  
    if not jobs:
      raise Exception()
    save_to_file(jobs)  
    return send_file("jobs.csv")
  except: 
    return redirect("/") 



#@app.route("/<username>") # @=데코레이터 파이썬이 위와 같은 코드를 보면 /contact 로 요청이 들어오면 밑에있는 함수를 실행시킨다 (함수만 봄)
#꺽쇠 부분은 placeholder
#def potato(username):
#  return f"Hello {username} how are you doing"

app.run(host="0.0.0.0") #repl.it이 이 사이트를 공개하고 싶구나 알수 있게하는 코드