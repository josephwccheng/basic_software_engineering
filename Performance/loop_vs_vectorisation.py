# comment from https://stackoverflow.com/questions/52673285/performance-of-pandas-apply-vs-np-vectorize-to-create-new-column-from-existing-c

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