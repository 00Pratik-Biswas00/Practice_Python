class Book:
    total_book=0
    def __init__(self, book_name):
        self.__name = book_name
        Book.total_book+=1  # Counting how many times the object is created
    
    @property # this is used to restrict in overwriting 
    def get_book(self):
        return self.__name
    
    @staticmethod   # Decorator
    def static_meth():
        return "This is a static method!"



my_book1 = Book("Nonte fonte")
my_book2 = Book("Thakumar jhuli")
# print(my_book1.__name) # name is private
print(my_book1.get_book())
print(Book.total_book)
print(Book.static_meth())

print(my_book1.get_book)