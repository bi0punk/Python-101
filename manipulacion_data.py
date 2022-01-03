from typing import Text
import bs4
import requests
import pandas as pd 


#obteniendo sitio en htnl

fuente_dat = 'http://www.sismologia.cl/ultimos_sismos.html'
page = requests.get(fuente_dat)
sopa = bs4.BeautifulSoup(page.text, 'lxml')
#obtenienod la tabla a partir del html
tabla = sopa.find('table')

cabezeras= []

for i in tabla.find_all('th'):
    title = i.text.strip()
    cabezeras.append(title)

df = pd.DataFrame(columns = cabezeras )

for filas in tabla.find_all('tr')[1:]:
    info = filas.find_all('td')
    filas_info = [td.text.strip() for td in info]
    length = len(df)
    df.loc[length] = filas_info

# ~ print(df) 

# ~ print(df.head(2)) # o n numeros..dependiendo dela necesidad...
# ~ print(df.tail()) 
# ~ print(df.sample()) # toma un registro al azar, si pasamos parametro sera el n de muestras

# ~ print(df.max["Latitud"])
# ~ print(df.describe()) 
# ~ prog_mag = df[["Profundidad [Km]", "Magnitud"]]
# ~ print(prof_mag)

prof = df["Magnitud"]

# ~ sis_prof = prof <= 100

print(prof) 
# ~ print(df["Profundidad [Km]"] >= -33 ) 
