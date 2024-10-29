#fichier contenant les données communes à tout le monde
import pandas as pd 
import geopandas as gpd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('world-country-electricity.csv')

np.sum(df.isna().to_numpy())




