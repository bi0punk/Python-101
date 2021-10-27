
import pandas as pd

df = pd.read_html('http://www.sismologia.cl/ultimos_sismos.html')

print(f'Total tables:  {len(df)}') 


df[0].to_csv('sismos.csv')