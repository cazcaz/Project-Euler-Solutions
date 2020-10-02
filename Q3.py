x=600851475143
primes=[2]
PrimeDivisors=[]
i=3
exit = False
while exit==False:
    for m in primes:
        if x%m == 0:
            PrimeDivisors.append(m)
            x = x//m
    PrimeCheck=True
    for j in primes:
        if i%j == 0:
            PrimeCheck = False
    if PrimeCheck == True:
        primes.append(i)
        if x%i ==0:
            x= x//i
            PrimeDivisors.append(i)
    if x == 1:
        exit = True
    i+=1
print(PrimeDivisors)

            




    



    