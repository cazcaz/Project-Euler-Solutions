def unit_convertor(x):
    lst=[]
    for i in range(0,len(str(x))):
        numberlst = str(x)
        lst.append(int(numberlst[i]))
    return lst

digitlst = unit_convertor(2**1000)
print(sum(digitlst))