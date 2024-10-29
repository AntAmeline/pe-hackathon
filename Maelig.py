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
#remplacer les "--" par Na
df.replace("--", np.nan, inplace=True)
#sous tableau de donnee
donnee = df.iloc[:,df.columns.get_loc('1980'):df.columns.get_loc('2021')]
#remplacer objet par float
for column in donnee.columns :
    donnee[column] = pd.to_numeric(donnee[column],errors = 'coerce')


# %%
by_Region = df.groupby(by = 'Region')

for region in df['Region'].unique():
    for feature in df['Features'].unique():
        
        mask_net_get_region_feature = by_Region.get_group(region)['Features'] == feature
        region_feature = by_Region.get_group(region)[mask_net_get_region_feature]

        region_feature.drop(columns = ['Country', 'Features', 'Region'] , inplace = True)

        for column in region_feature.columns :
            region_feature[column] = pd.to_numeric(region_feature[column], errors = 'coerce')
    
        plt.figure()
        region_feature.mean().plot()
        plt.xlabel((feature + " in " + region + " between 1980 and 2020"))
        plt.show()
        

# %%
def graph(df, region, feature) :
    by_Region = df.groupby(by = 'Region')
    mask_net_get_region_feature = by_Region.get_group(region)['Features'] == feature
    region_feature = by_Region.get_group(region)[mask_net_get_region_feature]

    region_feature.drop(columns = ['Country', 'Features', 'Region'] , inplace = True)

    for column in region_feature.columns :
        region_feature[column] = pd.to_numeric(region_feature[column], errors = 'coerce')
    
    plt.figure()
    region_feature.mean().plot()
    plt.xlabel((feature + " in " + region + " between 1980 and 2020"))
    plt.show()


# %%
graph(df,"Afrique","net generation")
