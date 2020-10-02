def reccuring_length(x):
    remainders = [1]
    remainder = 1
    evendivide = False
    while remainder != 0:
        remainder = (remainder*10)%x
        if remainder == 0:
            evendivide = True
        if remainder in remainders:
            remainder = 0
        remainders.append(remainder)
    remainders.pop()
    if evendivide == True:
        return 0
    else:
        return len(remainders)

max = 0

for i in range(1,1000):
    x=reccuring_length(i)
    if x > max:
        max = x
        print(i, x)

