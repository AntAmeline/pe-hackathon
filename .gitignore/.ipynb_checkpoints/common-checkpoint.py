#fichier contenant les données communes à tout le monde
import pandas as pd 
import geopandas as gpd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('world-country-electricity.csv')

np.sum(df.isna().to_numpy())



<<<<<<< HEAD:.gitignore/.ipynb_checkpoints/common-checkpoint.py
df = pd.read_csv('world-country-electricity.csv')
=======
>>>>>>> 4cd0823b2476e814bf847c16b4475558a701595c:.ipynb_checkpoints/common-checkpoint.py

