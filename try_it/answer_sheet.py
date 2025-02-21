# # Q1
#
# def string_filter(string):
# 	cleaned_string = ''
# 	for char in string:
# 		if char.isalpha() or char == ' ':
# 			cleaned_string += char
#
# 	for char in cleaned_string:
# 		if char == " ":
# 			print('\n', end='')
# 		else:
# 			print(char, end='')
#
# input_string = """He said, That's what he said!"""
# string_filter(input_string)

# Q2
#
# def reverse_string(string):
# 	words= []
# 	word = ''
# 	for char in string:
# 		if char == '.':
# 			words.append(word)
# 			words.append('.')
# 			word =''
# 		else:
# 			word += char
# 	words.append(word)
#
# 	left , right = 0, len(words) -1
# 	while left < right:
# 		words[left],words[right] = words[right], words[left]
# 		left +=1
# 		right -= 1
# 	return ''.join(words)
# string = "hello.world.this.is.python"
# print(reverse_string(string))  # Output: "python.is.this.world.hello"

# Q3
#pattern01
# def pascal_triangle(n):
# 	triangle =[]
# 	for i in range(n):
# 		row = [1] * (i+1)
# 		for j in range(1,i):
# 			row[j]= triangle[i-1][j-1]+triangle[i-1][j]
# 		triangle.append(row)
# 		print(" "*(n-i-1), end='')
# 		print(" ".join(map(str,row)))
# 	print(triangle)
#
#
# pascal_triangle(5)
#
# def pattern():
# 	for i in range(1,5+1):
# 		for j in range(1,5+1):
# 			print(max(j,i), end= '')
# 		print()
# pattern()

# def pattern(n):
# 	for i in range(1,n+1):
# 		for j in range(1,i+1):
# 			print(i*j, end= ' ')
# 		print()
# pattern(5)

# def pattern(n):
# 	for i in range(n):
# 		if i == 0:
# 			print(" "*(n-i)+"*"*(2*(i)+1))
# 		else:
# 			print(" "*(n-i)+ "*" + " " * (2*(i-1)+1)+ "*")
# pattern(5)

def subsets(arr):
	result = [[]]
	for i in arr :
		result += [j + [i] for j in result]
	return result

print(subsets([1,2,3]))
