def next_collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n +1
def collatz_length(n):
    length =1
    while n != 1:
        n = next_collatz(n)
        length +=1
    return length

max = 0
for i in range(1,1000001):
    temp = collatz_length(i)
    if temp > max:
        print(i, temp)
        max = temp

