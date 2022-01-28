import csv

def save_to_file(jobs):
  file=open("jobs.csv",mode="w")
  print(file)
  writer=csv.writer(file) #연 파일에다가 csv 작성
  writer.writerow(["title", "company", "location", "link"]) #writerow 함수를 통해 각 column 들의 첫번째 칸에 작성된다.
  for job in jobs:
    writer.writerow(list(job.values())) #job이 가진 list값을 row로 옮긴다
  return