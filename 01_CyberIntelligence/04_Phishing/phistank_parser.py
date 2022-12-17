
#Phistank es una página dónde se reportan casos de phishing
#Phistank no tiene abierta la opción para registrarse como usuario y poder utilizar la API del RSS
from urllib.request import urlopen
  
import json
url = "https://data.phishtank.com/data/online-valid.json"
  
response = urlopen(url)
data_json = json.loads(response.read())
  
out_file = open("phishings_list.json", "w")   
json.dump(data_json, out_file, indent = 6)
out_file.close()
