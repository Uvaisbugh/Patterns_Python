class PalindromeChecker:
	def __init__(self, text):
		self.text = text  # Store the string to be checked

	def is_palindrome(self):
		left = 0
		right = len(self.text) - 1

		while left < right:
			if self.text[left] != self.text[right]:
				return False
			left += 1
			right -= 1
		return True

	def __str__(self):
		return f"The text '{self.text}' is a palindrome: {self.is_palindrome()}"


# Example usage:
checker = PalindromeChecker("madam")
print(checker)  # Will print whether "madam" is a palindrome

checker2 = PalindromeChecker("hello")
print(checker2)  # Will print whether "hello" is a palindrome
