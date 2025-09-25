num = 10

try:
    assert num>10
    print("Number is greater than 10")
except AssertionError:
    print("Please enter a number greater than 10")