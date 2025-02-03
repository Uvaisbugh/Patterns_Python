string = "MalAyalam"
equivalent_chars = {'M': 'm', 'A': 'a'}

# Step 1: Create a dictionary to count characters
char_count = {}
for char in string:
    # Replace with equivalent lowercase if needed
    if char in equivalent_chars:
        char = equivalent_chars[char]
    # Count each character
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Step 2: Identify repeating characters
repeating_chars = {}
for char in char_count:
    if char_count[char] > 1:
        repeating_chars[char] = char_count[char]

print(repeating_chars)



def solu(s):
    rdic = {}
    rstr = ""
    for char in s:
        if 'A' <= char <= 'Z':
            rstr += chr(ord(char) + 32)
        else:
            rstr += char
    for char in rstr:
        if char in rdic:
            rdic[char] += 1
        else:
            rdic[char] = 1
    return {char: count for char, count in rdic.items() if count > 1}