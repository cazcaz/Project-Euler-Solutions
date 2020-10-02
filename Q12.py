import collections
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def no_divisors(n):
    counter=collections.Counter(prime_factors(n))
    temp=1
    for i in counter.values():
        temp = temp * (i+1)
    return temp

exit = False
i=1
max = 0
while exit == False:
    trianglenumber = (i*(i+1))//2
    x=no_divisors(trianglenumber)
    if x > max:
        max = x
        print(max)
        if max > 500:
            exit = True
            print(trianglenumber)
    i+=1

