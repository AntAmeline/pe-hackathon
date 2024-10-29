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

df['Features'].unique()

# +
by_Region = df_cleared.groupby(by = 'Region')
by_Year = df_cleared.groupby(by = 'Year')

for region in df['Region'].unique():
    for feature in df['Features'].unique():
        
        mask_net_get_region_feature = by_Region.get_group(region)['Features'] == feature
        region_feature = by_Region.get_group(region)[mask_net_get_region_feature]

        region_feature.drop(columns = ['Country', 'Features', 'Region'] , inplace = True)

        #for column in region_feature.columns :
         #   region_feature[column] = pd.to_numeric(region_feature[column], errors = 'coerce')
    
        plt.figure()
        region_feature.mean().plot()
        plt.xlabel((feature + " in " + region + " between 1980 and 2021"))
        plt.show()
        
#for feature in df_cleared['Feature'].unique():
#    mask_year = by_Year.get_group('2021')['Features'] == feature
    
# -


