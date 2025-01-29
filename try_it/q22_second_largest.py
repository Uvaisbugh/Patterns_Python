# def fibnocci(n):
# 	a, b = 0, 1
# 	while a < n:
# 		a, b = b, a + b
# 	return a == n


def found_larger(l):
	arr = list(set(l))
	arr.sort(reverse=True)
	return arr[1]


lists=[ 1,7,8,5,12,15]
print(found_larger(lists))


# def fibnacci(n):
# 	a, b = 0, 1
# 	while a < n :
# 		a, b = b, a+b
# 	return a ==n