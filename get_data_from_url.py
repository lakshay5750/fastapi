##now we have to get this data 
import requests
import json
import pandas as pd

response=requests.get("http://127.0.0.1:8000/twenty_min")
data=response.json()
data=data['candles']
print(data)

##convert the data and save to csv

# df=pd.DataFrame(data,columns=['timestamp','open','high','low','close','volume'])
# print(df.head(3))

# df.to_csv("twenty_min_data.csv")

##------------------------------------
##convert the data to json
with open('twenty_min_data.json','w') as f:
    json.dump(data,f,indent=4)


