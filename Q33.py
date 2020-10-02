def wrongfraction(lst):
    if lst[0] == lst[1]:
        return [1,1]
    numlst=[int(char) for char in str(lst[0])]
    denlst=[int(char) for char in str(lst[1])]
    numset = set(numlst)
    denset = set(denlst)
    cancels = list(numset.intersection(denset))
    for i in cancels:
        while len(numset) >= 1 and len(denset) >= 1:
            numlst.remove(i)
            denlst.remove(i)
    strnumlst = [str(s) for s in numlst]
    strdenlst = [str(s) for s in denlst]
    numerator = int("".join(strnumlst))
    denominator = int("".join(strdenlst))
    if denominator == 0:
        return lst
    return reducefract([numerator,denominator])

def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n

def reducefract(lst):
    n=lst[0]
    d=lst[1]
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return [int(n), int(d)]


    
    


