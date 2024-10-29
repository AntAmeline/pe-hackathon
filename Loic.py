# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from common import *

# %%
df.head(5)

# %%
df.size

# %%
df.shape

# %%
ratio_val_manquantes = 1177/1609*42
ratio_val_manquantes

# %%
by_country = df.groupby(by='Country')

# %%
df.isna()

# %%
nonval_pays = {}
for pays in df['Country'].unique() : 
    nonval_pays[pays] = by_country.get_group(pays).isna()   #.sum().sum()

# %%
nonval_pays['        Ukraine']

# %%
ukraine = by_country.get_group('        Ukraine')
ukraine

# %%
ukraine.isna()

# %%
df.isna().sum().sum()

# %%
True in np.array(df.isna())

# %%
True in np.array(ukraine.isna())

# %%
df.isna()['2020'].unique()

# %%
for i in df.index :
    if df.isna()['2020'].loc[i] == True :
        print(i)

# %%
df.isna()['2020'][138]

# %%
df.loc[138]

# %%
df.loc[68] 
