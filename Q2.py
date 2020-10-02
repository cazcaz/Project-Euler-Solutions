sum=2
fibs=[1,2]
while fibs[len(fibs)-1] < 4000000:
    nextfib = fibs[len(fibs)-1] + fibs[len(fibs)-2]
    fibs.append(nextfib)
    #print(nextfib)
    if nextfib % 2 ==0:
        sum+= nextfib
print(sum)