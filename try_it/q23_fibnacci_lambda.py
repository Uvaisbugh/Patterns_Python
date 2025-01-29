from functools import reduce

febnacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

n = 10
print(febnacci_series(n))
