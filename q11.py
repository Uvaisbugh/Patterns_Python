n=5
space = 0
for i in range(n,0,-1):
	print(' '*space,"* " * i )
	space +=1
for j in range(n+1):
	print(' '*space,"* " * j )
	space -=1
