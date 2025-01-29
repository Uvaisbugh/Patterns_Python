n = 5

# Upper half of the diamond
for i in range(n):
    if i == 0:
        print(" " * (n - i - 1) + "*" * ((2 * i) + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * ((2 * i) - 1) + "*")

# Lower half of the diamond
for i in range(n - 2, -1, -1):
    if i == 0:
        print(" " * (n - i - 1) + "*" * ((2 * i) + 1))
    else:
        print(" " * (n - i - 1) + "*" + " " * ((2 * i) - 1) + "*")
