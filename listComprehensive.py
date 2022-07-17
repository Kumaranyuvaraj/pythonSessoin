inp =[1,3,5,7]

x = [x**2 for x in inp]

x.insert(1, 3)
x.pop(2)
print(x)
