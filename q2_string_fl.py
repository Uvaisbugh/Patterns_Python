input_string = 'i.like.this.program.very.much'
# def q2(input_string: str) -> str:
#     return '.'.join(input_string.split('.')[::-1])
# print(q2(input_string))

#METHOD 2 without Built-in methods
string = input_string
def Solution_method(string):
	string = string.split('.')
	string = string[::-1]
	string = '.'.join(string)
	return string


print(Solution_method(string))

print("\n")

def solution_method(string):
	# Manually split the string by '.'
	words = []
	word = ""

	for char in string:
		if char == ".":
			words.append(word)  # Store word in list
			words.append(".")  # Store '.' separately
			word = ""  # Reset word
		else:
			word += char  # Append character to word

	words.append(word)  # Append the last word

	# Reverse the words manually
	left, right = 0, len(words) - 1
	while left < right:
		words[left], words[right] = words[right], words[left]
		left += 1
		right -= 1

	# Manually join the words
	result = ""
	for w in words:
		result += w

	return result


# Example usage
string = "hello.world.this.is.python"
print(solution_method(string))  # Output: "python.is.this.world.hello"
