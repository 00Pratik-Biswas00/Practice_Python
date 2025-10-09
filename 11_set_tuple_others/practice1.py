import collections
# 1 ------

# books_in_library = {"Book A", "Book B", "Book C", "Book D"}
# borrowed_books = {"Book B", "Book D"}

# print(f"Availiable books - {books_in_library-borrowed_books}")

# 2 -------

sentence = "python is easy and python is fun"
my_list = list(sentence.split(" "))
print(dict(collections.Counter(my_list)))

