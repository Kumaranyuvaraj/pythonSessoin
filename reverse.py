# x = "Boopathi"
# length = len(x)
# sliced = x[length::-1]
# print(sliced)



# x =[1,2,3,4,5]
# y =[]

# for items in x:
#     y.append(items*2)
# y.sort(reverse=True)
# print(y)

# print(sorted(i**2 for i in [5,4,3,2,1]))


x = 1234
y =0

while x!=0:
    z = x%10
    y = y * 10 + z
    x //=10
print("reversed number:" + str(y))



