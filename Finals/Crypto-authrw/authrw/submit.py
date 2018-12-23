import requests
import json

def submit_flag(flag):
   url = "http://10.115.0.2:8000/flag"
   data = json.dumps({"flag": flag})
   # if the team name is bi0s and password is bi0s - you need base64 of "bi0s:bi0s"
   # header = {"Authorization": "Basic YmkwczpiaTBz"}
   header = {"Authorization": "Basic <base64(team_name:team_password)>"}
   r = requests.post(url, data=data, headers=header)
   print r.text 
   
   return

submit_flag("sdadas")

