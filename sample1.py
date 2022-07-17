# string="aaawwccc"

# str_ = string[0]
# str_len = str(len(string[0:3]))
# con = str_+ str_len
# print (con)

# striii = string[3]
# element = str(len(string[3:5]))
# comb = striii + element
# print(comb)

# str_c = string[5]
# elements = str(len(string[5:9]))
# cons = str_c + elements
# print(cons)
# print(con+comb+cons)

# a = [1,2,3,4,5]
# a[0] = 5
# a[4] = 1
# print(a)

numbers = [1,2,3,4,4,3,6,7,1,2]

for i in range (len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])




