from collections import Counter\

def find_most_repeated(string):
	count = Counter(string)
	most_common_letter, count = count.most_common(1)[0]
	return most_common_letter, count


input = 'abbababbababcaabcbac'
print(find_most_repeated(input))
