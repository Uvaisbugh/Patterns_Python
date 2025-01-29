def reverse_second_half(array):

	mid = len(array) // 2

	array[mid:] = array[mid:][::-1]
	return array


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reverse_second_half(arr)
print(result)