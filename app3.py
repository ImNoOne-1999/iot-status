import pandas as pd
import json,requests,math
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
current_time = current_time.split(":")
# print(current_time)

col_list = ["Name", "MacID"]
df = pd.read_csv("f.csv", usecols=col_list)
response = requests.get('http://iotrest.herokuapp.com/api/devicefetcher')
# print(response.json())
macid = ''
for i in response.json():
    loginTime = i["loginTime"].split(":")
    # print(loginTime) 
    totalLogTime = int(loginTime[0])*3600 + int(loginTime[1])*60 + int(loginTime[2])
    totalCurrentTime = int(current_time[0])*3600 + int(current_time[1])*60 + int(current_time[2])
    if abs(totalCurrentTime-totalLogTime) <= 600:
        macid = i["macId"]

count = 0
for j in df.MacID:
    if j == macid:
        print("proceed"+macid)
        break
    else:
        count += 1

if count == len(df):
    print("Abort Process")