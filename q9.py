def pattern(n):
	stars= 2*n-1
	space= 0
	for i in range(n+1):
		print(' '*space + '*'* stars)
		stars -= 2
		space +=1


pattern(5)

# def pattern_x(n):
# 	for i in range(n,0,-1):
# 		space=1
# 		for j in range(i):
# 			print( "*"*j , end="")
# 		space +=1
# 		print()

# pattern_x(5)
