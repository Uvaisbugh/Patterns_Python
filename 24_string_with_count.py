def char_count(string):
	char_dict = {}  # Dictionary to store character counts

	# Count occurrences of each character
	for char in string:
		char_dict[char] = char_dict.get(char, 0) + 1

	# Print each character with its count
	for char, count in char_dict.items():
		print(f"'{char}' appears {count} times")


# Example usage
text = "hello world"
char_count(text)
