n=5

for i in range(4,0,-1):
	for j in range(1,i+1):
		print(j,end="*") if j != i else print(j, end="")
	print()