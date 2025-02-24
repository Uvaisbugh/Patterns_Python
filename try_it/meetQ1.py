input_string = "Malayalam"


def string_count(str):
	redic = {}
	restr = ""
	#filter
	for char in str:
		if 'A' <= char <= 'Z':
			restr += chr(ord(char) + 32)
		else:
			restr += char
	#count
	for char in restr:
		if char in redic:
			redic[char] += 1
		else:
			redic[char] = 1
	return {char: count for char, count in redic.items() if count > 1}


print(string_count(input_string))
