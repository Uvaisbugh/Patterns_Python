def pattern(n):
	for i in range(1,n+1):
		space= n - i
		print(" "* space, end='')
		for col in range(i,0,-1):
			print((chr)(n-col+64+1), end=' ')
		print()

pattern(5)