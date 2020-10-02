def sumfifthpowers(x):
    lst= [int(char) for char in str(x)]
    sum = 0
    for i in range(0,len(lst)):
        sum += lst[i]**5
    return sum

total = -1
for i in range(1,1000001):
    if i == sumfifthpowers(i):
        total += i 
    
print(total)