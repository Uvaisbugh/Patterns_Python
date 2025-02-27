from functools import reduce

febnacci_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

n = 10
print(febnacci_series(n))

# def febnacci(n):
#     if n <= 1:
#         return n
#     return febnacci(n-1) + febnacci(n-2)
# print(febnacci(9))

