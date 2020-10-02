#Plan; make a list of amicable numbers, then make a list of numbers that can be made from sums of two numbers in this list
#Add up numbers not in this list

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
abundantsone = []
abundantstwo = []
for i in range(1,28124):
    if d(i) > i:
        print(i)
        abundantsone.append(i)
        abundantstwo.append(i)

possibles = set()

for first in abundantsone:
    for second in abundantstwo:
        if first + second < 28124:
            possibles.add(first+second)

naturals = set(i for i in range(1,28124))

impossibles = naturals.difference(possibles)

print(sum(impossibles))
