from collections import Counter


def count_elements(arr):
	# Count the occurrences of each element using Counter
	counts = Counter(arr)

	# Print the element and its count
	for element, count in counts.items():
		print(f"{element}={count}")



arr = [1, 4, 5, 2, 1, 4]
count_elements(arr)
