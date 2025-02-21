String ="Malayalam"

def to_lowercase(string):
    result = ""
    for char in string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def count_repeating_letters(string):
    string = to_lowercase(string)
    letter_count = {}

    for char in string:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    
    return {char: count for char, count in letter_count.items() if count > 1}

# Example usage:
string = "Malayalam"
print(count_repeating_letters(string))

