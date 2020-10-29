import requests
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

response = requests.post('http://iotrest.herokuapp.com/api/statusfetcher', json={
    "macId" : "00-14-22-01-23-45",
    "statusTime" : current_time
})

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())