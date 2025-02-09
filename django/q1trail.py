input_string = "Malayalam"

# def solution(string):
#     string = string.lower()
#     return {char: string.count(char) for char in string if string.count(char) > 1}

def string_count(string):
    redict = {}
    restring = ""
    for char in string:
        if 'A' <= char <= 'Z':
            restring = chr(ord(char) + 32)
        else:
            restring += char
    for char in restring:
        if char in redict:
            redict[char] += 1
        else:
            redict[char] = 1
    return {char: count for char, count in redict.items() if count > 1}


print(string_count(input_string))