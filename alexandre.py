# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from common import *

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

# +
by_Region = df.groupby(by = 'Region')
#by_Year = df.groupby(by = 'Year')

for region in df['Region'].unique():
    for feature in df['Features'].unique():
        
        mask_net_get_region_feature = by_Region.get_group(region)['Features'] == feature
        region_feature = by_Region.get_group(region)[mask_net_get_region_feature]

        region_feature.drop(columns = ['Country', 'Features', 'Region'] , inplace = True)

        for column in region_feature.columns :
            region_feature[column] = pd.to_numeric(region_feature[column], errors = 'coerce')
    
        plt.figure()
        region_feature.mean().plot()
        plt.xlabel((feature + " in " + region + " between 1980 and 2021"))
        plt.show()
        
#for feature in df_cleared['Feature'].unique():
#    mask_year = by_Year.get_group('2021')['Features'] == feature
    
# -


