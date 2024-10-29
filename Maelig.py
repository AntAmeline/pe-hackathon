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

# %%




# %%
#remplacer les "--" par Na
df.replace("--", np.nan, inplace=True)
#sous tableau de donnee
donnee = df.iloc[:,df.columns.get_loc('1980'):df.columns.get_loc('2021')]
#remplacer objet par float
for column in donnee.columns :
    donnee[column] = pd.to_numeric(donnee[column],errors = 'coerce')

