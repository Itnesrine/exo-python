array = [10, 22, 64, 20, 1]
total = 0 

for i in range(len(array)):
    print(array[i])

for i in array: 
    print(i)


for var in array:
    total = total + var
print(total)        

total = 0
array[0] = 10
for var in range(len(array)):
    total = total + array[var]
print(total)    