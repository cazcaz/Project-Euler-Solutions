#Create a generating function for the number of ways 200p can be made with the 8 coins
#Let the computer work out the actual coefficient
#Done, easy peasy cheese with peas (and cake for moderation purposes)

#This keyboard is so nice to type on honestly wowee

#As the generating function isn't very funky, will make a system to let me multiply polynomials
#Then multiply the ones up to x^200 or above

#Find coefficient of x^200

#Define polynomials as lists of coefficients, lowest power first

def polymultiply(p,q):
    #p and q are polynomials
    lst = [0 for i in range(1, len(p)+len(q))]
    for i in range(0,len(p)):
        for j in range(0,len(q)):
            lst[i+j] += p[i]*q[j]
    return lst

target = 200

coll = {1: [], 2: [], 5: [], 10: [], 20: [], 50: [], 100: [], 200: []}

for i in range(0,(target//200 +1)*200+1):
    for val,lst in coll.items():
        if i % val == 0:
            lst.append(1)
        else:
            lst.append(0)

gen = polymultiply(coll[1], coll[2])
for key,val in coll.items():
    if key != 1 and key != 2:
        gen = polymultiply(gen, val)



# onepence = []
# twopence = []
# fivepence = []
# tenpence = []
# twentypence = []
# fiftypence = []
# hundredpence = []
# twohundredpence = []

# for i in range(0,(target//200 +1)*200+1):
#     if i%1 == 0:
#         onepence.append(1)
#     else:
#         onepence.append(0)
#     if i%2 == 0:
#         twopence.append(1)
#     else:
#         twopence.append(0)
#     if i%5 == 0:
#         fivepence.append(1)
#     else:
#         fivepence.append(0)
#     if i%10 == 0:
#         tenpence.append(1)
#     else:
#         tenpence.append(0)
#     if i%20 == 0:
#         twentypence.append(1)
#     else:
#         twentypence.append(0)
#     if i%50 == 0:
#         fiftypence.append(1)
#     else:
#         fiftypence.append(0)
#     if i%100 == 0:
#         hundredpence.append(1)
#     else:
#         hundredpence.append(0)
#     if i%200 == 0:
#         twohundredpence.append(1)
#     else:
#         twohundredpence.append(0)

# generatingfunction = polymultiply(onepence,twopence)
# generatingfunction = polymultiply(generatingfunction,fivepence)
# generatingfunction = polymultiply(generatingfunction,tenpence)
# generatingfunction = polymultiply(generatingfunction,twentypence)
# generatingfunction = polymultiply(generatingfunction,fiftypence)
# generatingfunction = polymultiply(generatingfunction,hundredpence)
# generatingfunction = polymultiply(generatingfunction,twohundredpence)

#Genereating function is correct up until the target value, then is incorrect as infinities have been avoided

print(gen[target])




