def check_fibonacci(n):
	a, b = 0, 1
	while a < n:
		a, b = b, a + b
	return a == n


num = int(input("number : "))
if check_fibonacci(num):
	print(f"{num} is a fibonacci number.")
else:
	print(f"{num} is not a fibonacci number.")
