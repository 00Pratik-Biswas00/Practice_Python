class Error(Exception):
    # Base class for custom exceptions
    pass

class dobException(Error):
    def __init__(self, message="Your age is not within the range"):
        self.message = message
        super().__init__(self.message)

year = int(input())
age = 2025-year

try:
    if age <=60 and age >=20:
        print("You are eligible for the scheme")
    else:
        raise dobException
except dobException as dob:
    print(dob)