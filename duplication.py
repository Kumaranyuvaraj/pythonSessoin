numbers = [1,2,3,4,2,4,5,6,1,10,10]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])
        

            

