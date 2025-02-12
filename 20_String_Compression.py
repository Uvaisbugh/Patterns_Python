def compress_string(input_string):
	# Initialize an empty string to store the compressed version
	compressed = ""
	count = 1

	# Iterate through the string
	for i in range(1, len(input_string)):
		if input_string[i] == input_string[i - 1]:
			# Increment the count if the current character matches the previous one
			count += 1
		else:
			# Append the character and its count to the compressed string
			compressed += input_string[i - 1] + str(count)
			count = 1  # Reset the count for the next character

	# Append the last character and its count
	compressed += input_string[-1] + str(count)

	# Return the compressed string
	return compressed


# Example usage
input_string = "aabcccccaaa"
compressed_string = compress_string(input_string)
print("Compressed string:", compressed_string)
