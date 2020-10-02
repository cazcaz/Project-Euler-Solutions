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

#Since the problem only deals with numbers up to 1,000,000, I will only make the binary convertor test up to 2^19
#Can be made general using logs and finding an upper bound with logs of base 2

def denary_binary(x):
    lst=[]
    for i in range(19, -1, -1):
        if x >= 2**i:
            x -= 2**i
            lst.append(1)
        else:
            lst.append(0)
    while lst[0] == 0:
        lst.pop(0)
    strlst = [str(s) for s in lst]
    number =  int("".join(strlst))
    return number

numbers=[]

for i in range(1,1000001):
    denary = i
    binary = denary_binary(i)
    if is_palindrome(denary):
        if is_palindrome(binary):
            print(denary, binary)
            numbers.append(i)

print(sum(numbers))