def sum_of_differences(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)

    # Calculate the sum of differences between consecutive elements
    diff_sum = 0
    for i in range(1, len(numbers)):
        diff_sum += numbers[i-1] - numbers[i]
    
    return diff_sum

# Example usage
numbers = [10, 20, 5, 40, 15]
result = sum_of_differences(numbers)

print("Sorted list in descending order:", numbers)
print("Sum of differences between consecutive elements:", result)
