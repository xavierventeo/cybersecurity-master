
from urllib.request import urlopen
  
import json
url = "https://data.phishtank.com/data/online-valid.json"
  
response = urlopen(url)
data_json = json.loads(response.read())
  
print(data_json)