def divisors(n):
    i=1
    lst=[]
    while i < n//2 +1:
        if n%i == 0:
            lst.append(i)
        i+=1
    return lst

def d(n):
    return sum(divisors(n))

amicables= []

for i in range(1,10000):
    x = d(i)
    if i == d(x) and i != x:
        print(i)
        amicables.append(i)

print(sum(amicables))
