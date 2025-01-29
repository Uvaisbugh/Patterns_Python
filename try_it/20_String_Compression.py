def compress_string(string):
	compressed = ""
	count = 1

	for i in range(1, len(string)):
		if string[i] == string[i - 1]:
			count += 1
		else:
			compressed += string[i - 1] + str(count)
			count = 1

	compressed += string[- 1] + str(count)
	return compressed


input_string = "aabcccccaaa"
compressed_string = compress_string(input_string)
print("Compressed string:", compressed_string)


















# def compressed_string(string):
# 	compressed = ""
# 	count = 1
#
# 	for i in range(1,len(string)):
# 		if string[i] == string[i-1]:
# 			count +=1
# 		else :
# 			compressed += string[i-1] + str(count)
# 			count = 1
# 	compressed += string[- 1] + str(count)
# 	return compressed
