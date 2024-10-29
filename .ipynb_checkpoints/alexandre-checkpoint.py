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
by_Region = df.groupby(by = 'Region')

mask_net_get_africa = by_Region.get_group('Africa')['Features'] == 'net generation'
net_gen_africa = by_Region.get_group('Africa')[mask_net_get_africa]

net_gen_africa
# -


