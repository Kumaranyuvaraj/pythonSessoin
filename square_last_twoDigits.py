

# inp = [1,2,3,4]
#o/p = [1,2,9,16]
# for i in inp:
#     if i>=3:
#         print(i**2)



# a = []
# y = [x**2 for x in inp]

# a.append(y)
# z = [x for b in a for x in b]
# z.insert(1, 2)
# z.pop(2)
# print(z)


inp = [1,2,3,4,5]

#o/p = [1,2,3,16,25]


x = [x**2 for x in inp]
x.insert(1, 2)
x.insert(2, 3)
x.pop(3)
x.pop(4)
print(x)




