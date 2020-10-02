def quadratic(a,b,x):
    return x**2 + a*x + b

def primetest(x):
    prime = True
    if x <= 1:
        return False
    if x % 2 == 0 and x!= 2:
        return False
    for i in range(3, int(x**0.5)+2):
        if x%i == 0:
            prime = False
    return prime

max = 0

for a in range(-999,1000):
    for b in range(-999,1000):
        i=0
        while primetest(quadratic(a,b,i)):
            i+=1
        if i > max:
            max = i
            print(a,b, max)


