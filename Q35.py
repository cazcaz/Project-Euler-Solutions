def is_prime(x):
    if x == 2:
        return True
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+2):
        if x%i == 0:
            return False
    return True

def numbercycler(x):
    if len(str(x)) == 1:
        return x
    numberlst = [char for char in str(x)]
    numberlstnew = []
    for i in range(1,len(numberlst)):
        numberlstnew.append(numberlst[i])
    numberlstnew.append(numberlst[0])
    return int("".join(numberlstnew))


circularprimes = []

for i in range(1,1000000):
    if is_prime(i) == True:
        lst=[]
        x=i
        for j in range(1,len(str(i))):
            x=numbercycler(x)
            lst.append(x)
        #print(lst + [i])
        circularprime = True
        zeroset = set()
        zeroset.add(0)
        numberset = set([int(char) for char in str(i)])
        intersect = zeroset.intersection(numberset)
        if intersect == zeroset:
            circularprime = False
        for k in lst:
            if is_prime(k) == False:
                circularprime = False
        if circularprime == True:
            circularprimes.append(i)

print(circularprimes)
print(len(circularprimes))





