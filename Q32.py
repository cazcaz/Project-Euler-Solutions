import collections

def pandigital_test(a,b):
    product = a*b
    lsta = [int(char) for char in str(a)]
    lstb = [int(char) for char in str(b)]
    lstproduct = [int(char) for char in str(product)]
    lst=[]
    lst += lsta
    lst += lstb
    lst += lstproduct
    frequency = list(collections.Counter(lst).values())
    values = set(collections.Counter(lst).keys())
    compareones = [1,1,1,1,1,1,1,1,1]
    comparevalues = set([1,2,3,4,5,6,7,8,9])
    if frequency == compareones and values == comparevalues:
        return True
    else:
        return False
    
pandigitals = set()

for a in range(1,10001):
    for b in range(1,10001):
        if pandigital_test(a,b):
            print(a,"*",b,"=",a*b)
            pandigitals.add(a*b)

print(pandigitals)