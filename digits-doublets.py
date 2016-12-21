from random import randint
from itertools import combinations

def factor(n):
    i = 1
    for j in range(1,n+1):
        i *= j
    return i
    
def checkio(data):    
    seq = []
    nCombo = 1
    n = len(str(data[0]))
    for i in range(1,n+1):
        nCombo *= i
    while len(seq) != nCombo:
        tmp = []
        while len(tmp) != n+1:            
            i = randint(0,n-1)             
            if i not in tmp:
                tmp.append(i)
            if len(tmp) == n:
                tmp.append(tmp[0])
        if tmp not in seq:
            seq.append(tmp)

    l_combo = data[1:len(data)-2]              
    print (nCombo, seq, l_combo)

    combo = []         
    i = 0
    """
    while i < int(factor(len(l_combo))/(factor(n)*factor(len(l_combo)-n))):
        tmp = []
        while len(tmp) != n:
            j = randint(0,len(l_combo)-1)
            if l_combo[j] not in tmp:
                tmp.append(l_combo[j])
            tmp.sort()
        if tmp not in combo:
            combo.append(tmp)
            i += 1
    """
    for e in combinations(l_combo,3):
        print (e)

    print (combo)
    print (factor(len(l_combo))/(factor(len(str(data[0])))*factor(len(l_combo)-len(str(data[0])))))

    
    
checkio([123, 991, 323, 321, 329, 121, 921, 125, 999])
