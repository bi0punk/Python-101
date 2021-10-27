from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url="http://www.sismologia.cl/links/ultimos_sismos.html"


html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "lxml")

df = pd.DataFrame(soup)
print(df)

#print(soup.prettify()) 

