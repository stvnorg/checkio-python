l = []

def gVar(n):
    global l
    if len(l)>=10:
        l = []
    for i in n:
        l.append(i)
    print (l)
    
if __name__ == '__main__':
    gVar([1,2,3])
    gVar([4,5,6,7])
    gVar([8,9,10,11])
    gVar([0])