
def string(s):
	upper = 0
	lower =0
	for char in s:
		if char.isupper():
			upper += 1
		elif char.islower():
			lower += 1
	return upper,lower

s = "The quick Brown Fox"
print(string(s))
