def unit_convertor(x):
    lst=[]
    for i in range(0,len(str(x))):
        numberlst = str(x)
        lst.append(int(numberlst[i]))
    return lst
def palindrome_test(lst):
    temp = True
    for i in range(0, len(lst)//2+1):
        if lst[i] != lst[len(lst)-i-1]:
            temp = False
    return temp
def is_palindrome(x):
    numberstr = unit_convertor(x)
    if palindrome_test(numberstr) == True:
        return True
    else:
        return False
#first palindrome above 100*100
largest=10001
for i in range (100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j) and i*j > largest:
            largest = i*j
print(largest)