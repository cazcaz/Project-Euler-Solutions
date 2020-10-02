def factorial(x):
    temp=1
    while x !=1:
        temp = temp * x
        x-=1
    return temp

def splitword(word):
    return [char for char in word]

hundredfac = str(factorial(100))
hundredfaclist = splitword(hundredfac)
sum = 0
for i in hundredfaclist:
    sum += int(i)

print(sum)
