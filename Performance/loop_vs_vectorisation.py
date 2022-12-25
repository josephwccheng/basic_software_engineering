# comment from https://stackoverflow.com/questions/52673285/performance-of-pandas-apply-vs-np-vectorize-to-create-new-column-from-existing-c
# https://numba.pydata.org/

import numpy as np
import pandas as pd
import timeit 

np.random.seed(0)
N = 10**5
number_iter = 2

A_list = np.random.randint(1, 100, N)
B_list = np.random.randint(1, 100, N)
df = pd.DataFrame({'A': A_list, 'B': B_list})
df.head()


def divide(a, b):
    if b == 0:
        return 0.0
    return float(a)/b


def divide_njit(a, b):
    res = np.empty(a.shape)
    for i in range(len(a)):
        if b[i] != 0:
            res[i] = a[i] / b[i]
        else:
            res[i] = 0
    return res


'''
False vectorisation

Below are all Python-level loops which produce either pd.Series, np.ndarray or list objects containing the same values
1. The tuple-based methods (the first 4) are a factor more efficient than pd.Series-based methods (the last 3).
2. np.vectorize, list comprehension + zip and map methods, i.e. the top 3, all have roughly the same performance. This is because they use tuple and bypass some Pandas overhead from pd.DataFrame.itertuples.
3. There is a significant speed improvement from using raw=True with pd.DataFrame.apply versus without. This option feeds NumPy arrays to the custom function instead of pd.Series objects.
Note:
- pd.DataFrame.apply: just another loop
- Creating, passing and querying a Pandas series object carries significant overheads relative to NumPy arrays.
- with raw=True and you'll see <class 'numpy.ndarray'>
np.vectorize: fake vectorisation
- The vectorized function evaluates pyfunc over successive tuples of the input arrays like the python map function, except it uses the broadcasting rules of numpy.
- np.vectorize converts your input function into a Universal function ("ufunc") via np.frompyfunc. There is some optimisation, e.g. caching, which can lead to some performance improvement.
- In short, np.vectorize does what a Python-level loop should do, but pd.DataFrame.apply adds a chunky overhead.

'''
list_map_time = timeit.timeit(lambda: list(map(divide, df['A'], df['B'])), number=number_iter)
numpy_vectorize_time = timeit.timeit(lambda: np.vectorize(divide)(df['A'], df['B']), number=number_iter)
dataframe_zip_time = timeit.timeit(lambda: [divide(a, b) for a, b in zip(df['A'], df['B'])], number=number_iter)
itertuples_time = timeit.timeit(lambda: [divide(a, b) for a, b in df[['A', 'B']].itertuples(index=False)], number=number_iter)
apply_raw_time = timeit.timeit(lambda: df.apply(lambda row: divide(*row), axis=1, raw=True), number=number_iter)
apply_no_raw_time = timeit.timeit(lambda: df.apply(lambda row: divide(row['A'], row['B']), axis=1), number=number_iter)
iterrows_time = timeit.timeit(lambda: [divide(row['A'], row['B']) for _, row in df[['A', 'B']].iterrows()], number=number_iter)

print(f'list_map_time: {list_map_time/number_iter} seconds')
print(f'numpy_vectorize_time: {numpy_vectorize_time/number_iter} seconds')
print(f'dataframe_zip_time: {dataframe_zip_time/number_iter} seconds')
print(f'itertuples_time: {itertuples_time/number_iter} seconds')
print(f'apply_raw_time: {apply_raw_time/number_iter} seconds')
print(f'apply_no_raw_time: {apply_no_raw_time/number_iter} seconds')
print(f'iterrows_time: {iterrows_time/number_iter} seconds')


'''
Real vectorisation

Why aren't the above differences mentioned anywhere? Because the performance of truly vectorised calculations make them irrelevant:
'''

np_where_time = timeit.timeit(lambda: np.where(df['B'] == 0, 0, df['A'] / df['B']), number=number_iter)
np_where_time_2 = timeit.timeit(lambda: (df['A'] / df['B']).replace([np.inf, -np.inf], 0), number=number_iter)

njit_time = timeit.timeit(lambda: divide_njit(df['A'].values, df['B'].values), number=number_iter)

print('Real Vectorisation')
print(f'np_where_time: {np_where_time/number_iter} seconds')
print(f'np_where_time_2: {np_where_time_2/number_iter} seconds')
print(f'njit_time: {njit_time/number_iter} seconds')