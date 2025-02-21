def count_word_occurrences(file_path):
    word_count = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.lower().replace('.', '').replace(',', '').split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1  # Count words

        return word_count

    except FileNotFoundError:
        print("Error: File not found.")
        return {}

# Example usage
file_path = "sample.txt"  # Replace with your file path
print(count_word_occurrences(file_path))
