def testRoute(n,j,data):
    U = [n[0]-1,n[1]]
    D = [n[0]+1,n[1]]
    R = [n[0],n[1]+1]
    L = [n[0],n[1]-1]
    if U == j:
        if data[U[0]][U[1]] == 'B': return 'B'
        elif data[U[0]][U[1]] == 'E': return 'E'
        return 'U'
    elif D == j:
        if data[D[0]][D[1]] == 'B': return 'B'
        elif data[D[0]][D[1]] == 'E': return 'E'
        return 'D'
    elif R == j:
        if data[R[0]][R[1]] == 'B': return 'B'
        elif data[R[0]][R[1]] == 'E': return 'E'
        return 'R'
    elif L == j:
        if data[L[0]][L[1]] == 'B': return 'B'
        elif data[L[0]][L[1]] == 'E': return 'E'
        return 'L'
    return 0

def checkio(data):
    test = 'SB.E'
    coord = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] in test:
                coord.append([i,j])

    path = [[coord[0]]]
    for i in path:
        n = i[len(i)-1]
        l = [m for m in coord if m not in i]
        for j in l:
            flag = testRoute(n,j,data)
            if flag:
                #print (flag)
                t = [m for m in i]
                x = j
                x.append(flag)
                t.append(x)
                #print (t)
                path.append(t)
                #print (path)
                #return 0
    
    routes = []
    for i in path:
        tmp = [n[2] for n in i[1:]]
        routes.append("".join(tmp))
        #if 'E' in tmp:
        #    routes.append(''.join(tmp))

    #print (coord, path)
    print (routes)

checkio(["S...","....","B.WB","..WE"])
checkio(["S..E","WWWW","WWWW","WWWW"])
