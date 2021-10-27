from typing import Text
import bs4
import requests
import pandas as pd 

df = pd.read_table("http://www.sismologia.cl/ultimos_sismos.html")

print(df)