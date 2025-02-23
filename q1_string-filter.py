input_string= """He said, That's what he said!"""

# def string_filter(input_string: str) -> str:
#     cleaning = input_string.replace('"',' ').replace('!','').replace(',','').replace("'",'')
#     words = cleaning.split()
#     for word in words:
#         print(word)
#
# print(string_filter(input_string))
#
# print("\n")
#METHOD 2 without Built-in methods
string = input_string
    
def Solution_method(string): 
    cleaned = ''
    for char in string:
        if char.isalpha() or char == ' ':
            cleaned += char


    for char in cleaned:
        if char == ' ':
            print('\n')
        else:
            print(char, end='')
    
    
    
print(Solution_method(string))

        