from functools import partial


def base_func(a, b, c):
    print(f'{a} {b} {c}')


part_func = partial(base_func, c=2)

part_func('a', 'b')
