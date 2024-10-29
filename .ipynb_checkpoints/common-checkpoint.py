#fichier contenant les données communes à tout le monde
import pandas as pd 
import geopandas as gpd 


df_orig = pd.read_csv('world-country-electricity.csv')
#sans valeur fausse
df_cleared=df_orig.dropna(how='all')
df_cleared=df_cleared.apply(pd.to_numeric, errors='coerce')
#réorganisation
df_byfeature=df_cleared.drop('Region', axis=1)
df_byfeature=df_byfeature.set_index('Features')
df_bycountry=df_cleared.drop('Region', axis=1)
df_bycountry=df_bycountry.set_index('Country')
df_cleared.dtypes

 #par région
df_byregion=df_byregion.pivot_table(index=['Region','Features'],aggfunc='sum', fill_value=0)
df_byregion


