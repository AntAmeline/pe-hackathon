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
ratio_val_manquantes = 5945/(1609*42)
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

# %%
#nouvelle tentative

# %%
for column in df_cleared.columns[3:]:
    df_orig[column]=pd.to_numeric(df_cleared[column], errors='coerce')

# %%
df_orig.isna().sum().sum()

# %%
df_orig.loc[68]

# %%
by_country = df_orig.groupby(by='Country')

# %%
nonval_pays = {}
for pays in df_orig['Country'].unique() : 
    nonval_pays[pays] = by_country.get_group(pays).isna().sum().sum()

# %%
print(nonval_pays)

# %%
argmax = []
max = 294
for k in nonval_pays : 
    if nonval_pays[k] == max : 
        argmax.append(k)
print(argmax, max)
    

# %%
nonval_pays['        Tuvalu']

# %%
tuvalu = by_country.get_group('        Tuvalu')
tuvalu
