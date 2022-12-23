'''
Tutorial from https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.GroupBy.apply.html

'''

import pandas as pd

df = pd.DataFrame({'A': 'a a b'.split(),
                   'B': [1,2,3],
                   'C': [4,6,5]})
g1 = df.groupby('A', group_keys=False)
g2 = df.groupby('A', group_keys=True)

g3 = g1[['B', 'C']].apply(lambda x: x / x.sum())
g4 = g2[['B', 'C']].apply(lambda x: x / x.sum())

g5 = g1[['B', 'C']].apply(lambda x: x.astype(float).max() - x.min())
g6 = g2[['B', 'C']].apply(lambda x: x.astype(float).max() - x.min())
print("done")