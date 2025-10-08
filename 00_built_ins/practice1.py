# default none if list is empty
l = []
print(min(l,default=None))

# unzipped
p = (2,3)
y = ("s", "d")
zipped = list(zip(p,y))
print(zipped)

if zipped:
    p_un, y_un = zip(*zipped)
    print(p_un)
    print(y_un)
else:
    print("----")

# sort a list of dict by last name then first name
my_dict = {1: "Pratik Biswas", 2: "Chandrima Kar", 3:"Ayaan Ahmed"}
sorted_dict = sorted(my_dict.items(), key=lambda item: (item[1].split()[-1], item[1].split()[0]))

print(sorted_dict)

