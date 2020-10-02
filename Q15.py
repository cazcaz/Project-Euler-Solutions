#Since the problem is just how many ways can you move down 20 ways and right 20 ways, it is simply the rearrangements of 20 Rs and 20 Ds
def factorial(x):
    temp=1
    while x !=1:
        temp = temp * x
        x-=1
    return temp

print(factorial(40)/(factorial(20)**2))

