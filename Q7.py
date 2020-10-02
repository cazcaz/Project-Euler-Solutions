primes = [2]
i=3
while len(primes)<10001:
    primeTest = True
    if i%2 == 0:
        primeTest = False
    if primeTest == True:
        exit =False
        m=0
        while exit == False:
            j=primes[m]
            if j**2 <= i:
                if i%j == 0:
                    primeTest = False
                    exit = True
            m+=1
            if m==len(primes):
                exit=True
    if primeTest == True:
        print(i)
        primes.append(i)
    i+=1

print(primes)