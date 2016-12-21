def CheckPath(n,j,data):
    E = [n[0],n[1]+1]
    W = [n[0],n[1]-1]
    N = [n[0]-1,n[1]]
    S = [n[0]+1,n[1]]
    if E == j:
        #print ('E')
        return True,'E'
    elif W == j:
        #print ('W')
        return True,'W'
    elif N == j:
        #print ('N')
        return True,'N'
    elif S == j:
        #print ('S')
        return True,'S'
    return False,'0'

def checkio(data):
    coord = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                coord.append([i,j])
    #print (coord)
    path = [[coord[0]]]
    for i in path:
        n = i[len(i)-1]
        #print (n)
        l = [m for m in coord if m not in i]
        for j in l:
            #print (n,j)
            valid,flag = CheckPath(n,j,data)
            if valid:
                t = [m for m in i]
                x = j
                x.append(flag)
                t.append(x)
                path.append(t)
    
    routes = []
    for i in path:
        if ([10,10,'E'] in i) or ([10,10,'W'] in i) or ([10,10,'N'] in i) or ([10,10,'S'] in i):
            labyrinth = [m[2] for m in i[1:]]
            routes.append("".join(labyrinth))
    print (routes)
            #return "".join(labyrinth)
            #break
            
    #print (coord, path)
    #print (path)


checkio([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

checkio([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]])
    
