import pandas as pd
import json,requests

col_list = ["Name", "MacID"]
df = pd.read_csv("f.csv", usecols=col_list)
for i in df.MacID:
    response = requests.get('http://iotrest.herokuapp.com/api/statusfetcher?macid='+i)
    if(response!=None):
        print("proceed")
    else:
        print("u can't proceed ")