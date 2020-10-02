def factorial(x):
    if x == 0:
        return 1
    temp=1
    while x > 0:
        temp = temp*x
        x-=1
    return temp

numbers = []

for i in range(3,10000000):
    temp = [int(char) for char in str(i)]
    sum=0
    for j in temp:
        sum += factorial(j)
    if sum == i:
        numbers.append(i)

print(numbers)



