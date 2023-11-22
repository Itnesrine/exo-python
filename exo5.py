mot = "radar"
array = list(mot)
count = len(array)
est_palindrome = True
result = ''
for i in range(count):
    result = result + array[count-(i+1)]
if mot == result :
    print(True)

else :
    print("le mot n'est pas un palindrome")
 
result = ''
for i in array :
     result = i + result
if mot == result :
    print(True)
else : 
    print(False)       












