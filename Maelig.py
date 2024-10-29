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
def graph_feature_by_region(df, region, feature) :
    #masque
    by_Region = df.groupby(by = 'Region')
    mask_net_get_region_feature = by_Region.get_group(region)['Features'] == feature
    region_feature = by_Region.get_group(region)[mask_net_get_region_feature]
    #clear valeurs manquantes
    region_feature.drop(columns = ['Country', 'Features', 'Region'] , inplace = True)
   
    plt.figure()
    #moyenne
    region_feature.mean().plot()
    plt.xlabel((feature + " in " + region + " between 1980 and 2020"))
    plt.show()


# %%
graph_feature_by_region(df_cleared, "Africa", "net generation")


# %%
def graph_feature_by_country(df, country, feature) :
    #masque
    by_feature = df.groupby(by = 'Features')
    mask_feature_by_country = by_feature.get_group(feature)['Country'] == country
    country_feature = by_feature.get_group(feature)[mask_feature_by_country]
    
    #clear valeurs manquantes
    country_feature.drop(columns = ['Country', 'Features', 'Region'] , inplace = True)
    
    plt.figure()
    #moyenne
    country_feature.mean().plot()
    plt.xlabel((feature + " in " + country + " between 1980 and 2020"))
    plt.show()


# %%
graph_feature_by_country(df_cleared, "Algeria", "net generation")

# %%

# %%
