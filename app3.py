import pandas as pd
import json,requests
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
current_time = current_time.split(":")
print(current_time)

col_list = ["Name", "MacID"]
df = pd.read_csv("f.csv", usecols=col_list)
response = requests.get('http://localhost:5000/api/devicefetcher')
# print(response.json())
macid = ''
for i in response.json():
    loginTime = i["loginTime"].split(":")
    #print(loginTime) 
    if (int(loginTime[0]) == int(current_time[0])) and (int(current_time[1]) - int(loginTime[1] ) >= int(current_time[1])):
        macid = i["macId"]

count = 0
for j in df.MacID:
    if j == macid:
        print("proceed")
        count += 1
        break

if count == len(response.json()):
    print("Abort Process")