def finish_map(m):
    m=list(m)
    d=[[[i,j]] for i in range(len(m)) for j in range(len(m[0])) if m[i][j]=='D']
    i = 0
    while i<len(d):
        x = d[i]
        for j in range(len(x)):
            y = x[j]
            print (m[y[0]][y[1]])
        i+=1
    print (d)

if __name__ == '__main__':
    finish_map(("D..XX.....",
                "...X......",                    
                ".......X..",
                ".......X..",
                "...X...X..",
                "...XXXXX..",
                "X.........",
                "..X.......",
                "..........",
                "D...X....D"))
