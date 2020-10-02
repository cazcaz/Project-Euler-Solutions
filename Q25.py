current=1
previous=1
i=2
while len(str(current)) < 1000:
    temp = current
    current += previous
    previous = temp
    i+=1

print(i)