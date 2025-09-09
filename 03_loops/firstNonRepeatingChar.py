enter_string = input("Enter string: ")

for char in enter_string:
    if enter_string.count(char) == 1:
        print(char)
        break