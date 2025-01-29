def sum_of_differences(num):
	num.sort(reverse=True)

	diff_sum = 0
	for i in range(1,len(num)):
		diff_sum +=num[i-1]-num[i]

	return diff_sum



numbers = [10, 20, 5, 40, 15]
result = sum_of_differences(numbers)

print("Sorted list in descending order:", numbers)
print("Sum of differences between consecutive elements:", result)
