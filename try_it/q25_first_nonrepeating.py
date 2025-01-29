def first_non_repeating(are):
	e_dic = {}
	for num in are:
		e_dic[num] = e_dic.get(num, 0) + 1

	for num in are:
		if e_dic[num] == 1:
			return num
	return None


arr = [4, 5, 1, 2, 0, 5, 1, 2]
print("First non-repeating element:", first_non_repeating(arr))

print()

from collections import OrderedDict


def first_non_repeatings(arr):
	count = OrderedDict()

	for num in arr:
		count[num] = count.get(num, 0) + 1

	for num in count:
		if count[num] == 1:
			return num

	return None


# Example usage
arr = [4, 5, 1, 2, 0, 5, 1, 2]
print("First non-repeating element:", first_non_repeatings(arr))
