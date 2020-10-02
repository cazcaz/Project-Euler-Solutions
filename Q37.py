def is_prime(x):
    if x == 2:
        return True
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+2):
        if x%i == 0:
            return False
    return True

def truncate_left(x):
    if x<10:
        return x
    numberlst = [s for s in str(x)]
    numberlst.pop(0)
    return int("".join(numberlst))

def truncate_right(x):
    if x<10:
        return x
    numberlst = [s for s in str(x)]
    numberlst.pop()
    return int("".join(numberlst))

numbers=[]
i=8
while len(numbers) < 11:
    leftx = i
    rightx = i
    leftprime = True
    rightprime = True
    leftexit = False
    rightexit = False
    if is_prime(i) == True:
        while leftprime and leftexit == False:
            leftx = truncate_left(leftx)
            if leftx < 10:
                leftexit = True
            if is_prime(leftx) == False:
                leftprime = False
        while rightprime and rightexit == False:
            rightx = truncate_right(rightx)
            if rightx < 10:
                rightexit = True
            if is_prime(rightx) == False:
                rightprime = False
        if rightprime and leftprime:
            numbers.append(i)
            print(len(numbers))
    i+=1
        
print(sum(numbers))

