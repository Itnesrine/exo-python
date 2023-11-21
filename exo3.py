array = [3,58,11,21]
maxvalue = array[0]
for var in range(len(array)):
    if array[var] > maxvalue :
        maxvalue = array[var]
print (maxvalue)             
maxvalue = 0
for var in array :
    if var > maxvalue :
        maxvalue = var
print (maxvalue)        


