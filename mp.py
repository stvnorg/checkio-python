def checkio(pattern, image):
    matrix = []
    for i in image:
        matrix.append(i)
	
    pattern_coord = []
    for i in range(len(pattern)):
	    for j in range(len(pattern[i])):
		    coord = [i,j,pattern[i][j]]
		    pattern_coord.append(coord)
			
    x = 0
    y = 0
    flag = False
			
    while x < len(matrix)-len(pattern):
        flag = False
        while y <= len(matrix[x])-len(pattern[0]):
            if matrix[x][y] == pattern[0][0]:
                for i in pattern_coord:
                    if matrix[x+i[0]][y+i[1]] == i[2]:
                        flag = True
                    else:
                        flag = False
                        break
            if flag:
                for i in pattern_coord:
                    if matrix[x+i[0]][y+i[1]] == 1:
                       matrix[x+i[0]][y+i[1]] = 3
                    else:
                       matrix[x+i[0]][y+i[1]] = 2
                y = 0
                flag = False
            elif flag == False:
            	y += 1
        x +=1
        y = 0
    
    print (matrix)
    return matrix

print (checkio([[1, 1], [1, 1]],
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]))