try:
    a=int(input("num 1: "))
    b=int(input("num 2: "))
    c=a+b
except ValueError as ne:
    print("try to enter integer values")
except TypeError as te:
    print("try to make the datatype similar")
except Exception as ex: # Parent class should be there at the end
    print(ex)
else:
    print(c)    # if try block exectues it'll be printed
finally:
    print("Execution is done!") # after execution is completed whether it's an error or not the finally block will be printed.