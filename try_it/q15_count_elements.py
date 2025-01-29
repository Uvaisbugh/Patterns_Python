from collections import Counter

def count_elements(ar):
	count= Counter(ar)

	for elment,count in count.items():
		print(f"{elment}={count}")



arr = [1, 4, 5, 2, 1, 4]
count_elements(arr)
