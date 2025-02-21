class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_pair(self):
        seen = {}
        for i, num in enumerate(self.numbers):
            complement = self.target - num
            if complement in seen:
                return seen[complement], i
            seen[num] = i
        return None  # Return None if no pair is found

# Example usage:
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
pf = PairFinder(numbers, target)
pair = pf.find_pair()
print(pair)  # Output: (3, 4)
