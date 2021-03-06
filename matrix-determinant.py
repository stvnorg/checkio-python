def determinant(matrix):
    return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])

def pMatrix(matrix,n):
    if len(matrix)==2:
        return determinant(matrix)
    else:
        result = []
        for i in range(1,len(matrix)):
            tmp = []
            for j in range(len(matrix[0])):
                if j!=n:
                    tmp.append(matrix[i][j])
            result.append(tmp)
    return result    
    
def checkio(matrix):
    if len(matrix)==2:
        return determinant(matrix)
    else:
        result = []
        for i in range(len(matrix[0])):
            result.append([matrix[0][i],checkio(pMatrix(matrix,i))])
    return result
                

if __name__ == '__main__':
    print (checkio([[4,3], [6,3]]))
    print (checkio([[1, 3, 2],[1, 1, 4],[2, 2, 1]]))
    print (checkio([[3, 0, 2, -1],[1, 2, 0, -2],[4, 0, 6, -3],[5, 0, 2, 0]]))