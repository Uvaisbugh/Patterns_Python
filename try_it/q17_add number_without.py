def add_numbers(a, b):
    while b != 0:
        a += 1
        b -= 1
    return a

# Example usage
num1 = 5
num2 = 7
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")

#
# def add_numbers(a, b):
# 	# Loop until there is no carry
# 	while b != 0:
# 		# Calculate carry and shift it left by one position
# 		carry = a & b
# 		a = a ^ b  # Sum without carry
# 		b = carry << 1  # Carry shifted by 1 to be added in the next iteration
#
# 	return a
#
#
# # Example usage
# num1 = 5
# num2 = 7
# result = add_numbers(num1, num2)
# print(f"The sum of {num1} and {num2} is {result}")
