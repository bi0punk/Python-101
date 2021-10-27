

import urllib.request, json 
import pandas as pd
import json
from bs4 import BeautifulSoup
import requests


resp = requests.get('https://farmanet.minsal.cl/index.php/ws/getLocalesTurnos')
txt = resp.json()
df = pd.DataFrame(txt)
""" df.to_csv('farma.csv') """
farma = df.head(70)[["localidad_nombre", "local_nombre", "local_direccion"]]
vall = df.iloc[22, [5,6,8,11]] # representa [filas,columnas]
print(vall)

