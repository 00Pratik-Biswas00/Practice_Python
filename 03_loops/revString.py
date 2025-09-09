enter_string = input("Enter string: ")

print(enter_string[::-1])

rev_string = ""
for char in enter_string:
    rev_string = char + rev_string
print(rev_string)