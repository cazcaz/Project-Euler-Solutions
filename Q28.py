#Thinking in shells, outer layer diagonals of an nxn spiral are 4n^2 - 6(n-1)
#Sum the shells from n=3 to n=1001 (n has to be odd)
#Add one for the centre

spiral_size = 1001  #ODD
index = (spiral_size + 1)//2
sum = 1
for i in range(2,index+1):
    oddindex = 2*i -1
    sum += 4*oddindex**2 - 6*(oddindex -1)

print(sum)


