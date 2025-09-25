li1 = ["pratik", "chandrima", "ayaan"]
li2 = [1,2,3]
li3 = ['a', 'b', 'c']

new_list = zip(li1,li2, li3)
print(new_list) # <zip object at 0x000002D505B48FC0>

for item in new_list:
    print(item) # same indexes tuple