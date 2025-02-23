# def find_longest_shortest_words(word_list):
#     if not word_list:
#         return None, None  # Return None if the list is empty
    
#     # Initialize the longest and shortest words
#     longest_word = shortest_word = word_list[0]
    
#     for word in word_list:
#         if len(word) > len(longest_word):
#             longest_word = word
#         elif len(word) < len(shortest_word):
#             shortest_word = word
            
#     return longest_word, shortest_word

# # Example usage
# word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
# longest, shortest = find_longest_shortest_words(word_list)

# print("Longest word:", longest)  # Output: airplane
# print("Shortest word:", shortest)  # Output: apple


print("\n")

def find_longest_shortest_words(word_list):
    longest_word = max(word_list, key=len)
    shortest_word = min(word_list, key=len)
    return longest_word, shortest_word

# Example usage
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
longest, shortest = find_longest_shortest_words(word_list)

print("Longest word:", longest)  # Output: airplane
print("Shortest word:", shortest)  # Output: apple
