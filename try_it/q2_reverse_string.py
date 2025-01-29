
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
	print(words)

	# Manually join the words
	result = ""
	for w in words:
		result += w

	return result


# Example usage
string = "hello.world.this.is.python"
print(solution_method(string))  # Output: "python.is.this.world.hello"
