import urllib.request
import json
import pandas as pd
import requests

url = 'https://farmanet.minsal.cl/index.php/ws/getLocalesTurnos'
resp = requests.get(url)
data = resp.json()

df = pd.DataFrame(data)
farma = df.head(70)[["localidad_nombre", "local_nombre", "local_direccion"]]
vall = df.loc[22, ["localidad_nombre", "local_nombre", "local_direccion"]]
print(vall)
