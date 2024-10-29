#fichier contenant les données communes à tout le monde
import pandas as pd 
import geopandas as gpd 
import numpy as np
import matplotlib.pyplot as plt




df_orig = pd.read_csv('world-country-electricity.csv')
#sans valeur fausse, numérisé
df_cleared=df_orig.dropna(how='all')
for column in df_cleared.columns[3:]:
    df_cleared[column]=pd.to_numeric(df_cleared[column], errors='coerce')
#problème des
#réorganisation
df_byfeature=df_cleared.drop('Region', axis=1)
df_byfeature=df_byfeature.set_index('Features')
df_bycountry=df_cleared.drop('Region', axis=1)
df_bycountry=df_bycountry.set_index('Country')
df_orig.head(10)

 #par région
df_byregion=df_cleared.pivot_table(index=['Region','Features'],aggfunc='sum', fill_value=0)








