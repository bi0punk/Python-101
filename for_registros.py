


from typing import Text
import bs4
import requests
import pandas as pd 


#obteniendo sitio en htnl

fuente_dat = 'http://www.sismologia.cl/ultimos_sismos.html'
page = requests.get(fuente_dat)
sopa = bs4.BeautifulSoup(page.text, 'lxml')
""" print(sopa)  """


tabla = sopa.find('table')

sismos = list()
cabezeras= []

for i in tabla.find_all('th'):
    title = i.text.strip()
    cabezeras.append(title)

df = pd.DataFrame(columns = cabezeras )

contador = 0



for filas in tabla.find_all('td'):
    info = filas.find_all('td')
    if contador < 7:
        filas_info = [td.text.strip() for td in info]
        sismos.append(filas_info)
    else:
        break
    contador += 1

print(sismos)




""" 
for filas in tabla.find_all('tr')[1:]:
    info = filas.find_all('td')
    filas_info = [td.text.strip() for td in info]
    length = len(df)
    df.loc[length] = filas_info

print(df) """