username = "Pratik"

username = "Pratik Biswas"
print(username)

x=10
y=x
print(x,y) # 10 10
x=15
print(x,y) # 15 10 (because y's reference is still on 10)
y=x
print(x,y) # 15 15

# username[0]="A" # in-place modification not possible

h1=[1,2,3]
h2=h1 # refers h1
print(h1,h2)
h1[0]=89 # changes will reflect on both files
print(h1,h2)    # [89, 2, 3] [89, 2, 3]
h3=h1[:]
print(h1,h3) # don't refer h1, instead create a copy
h1[0]=20    # thus changes will reflect only on h1
print(h1,h3)    # [20, 2, 3] [89, 2, 3]

h4=h1[:]
print(h1==h4) # checks value (True)
print(h1 is h4) # checks memory reference (False)