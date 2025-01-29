
def find_longest_shortest_words(wordlist):
	shortest = min(wordlist, key=len)
	longest = max( wordlist, key=len)
	return longest, shortest

word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
longest, shortest = find_longest_shortest_words(word_list)

print("Longest word:", longest)  # Output: airplane
print("Shortest word:", shortest)  # Output: apple
