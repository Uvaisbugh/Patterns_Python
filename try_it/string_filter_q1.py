def string_filter(string):
    # Clean the string to keep only alphabetic characters and spaces
    cleaned = ""
    for char in string:
        if char.isalpha() or char == ' ':
            cleaned += char


    # Print the cleaned string with newlines for spaces
    for char in cleaned:
        if char == " ":
            print("\n", end='')  # Print a newline when space is encountered
        else:
            print(char, end='')  # Print characters without newlines

input_string = """He said, That's what he said!"""
string_filter(input_string)
