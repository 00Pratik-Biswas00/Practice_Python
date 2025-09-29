print("Top-level code in module1 is running")

def hello():
    print("Hello from module1!")

# print("module1 is running directly")
# hello()
if __name__ == "__main__":
    print("module1 is running directly")
    hello()