#fichier contenant les données communes à tout le monde
import pandas as pd 
import geopandas as gpd 
import numpy as np
import matplotlib.pyplot as plt


# +
df_orig = pd.read_csv('world-country-electricity.csv')
#sans valeur fausse
df_cleared=df_orig.dropna(how='all')

#réorganisation
df_byfeature=df_cleared.drop('Region', axis=1)
df_byfeature=df_byfeature.set_index('Features')
df_bycountry=df_cleared.drop('Region', axis=1)
df_bycountry=df_bycountry.set_index('Country')
df_bycountry.head(3)
# -


