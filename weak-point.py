def weak_point(array):
	h,v = [],[]
	for i in range(len(array)):
		h.append(sum([array[i][j] for j in range(len(array[i]))]))
	for i in range(len(array[0])):
		v.append(sum([array[j][i] for j in range(len(array))]))
	h_min = h.index(min(h))
	v_min = v.index(min(v))
	print v_min
	for i in range(len(array[h_min])):
		if array[h_min][i] == array[h_min][v_min] and i==v_min: print [h_min,i]

if __name__ == '__main__':
	weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]])
			
	weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]])

	weak_point([[8,4,4,8,8,5,8],[2,9,1,5,7,3,1],[7,1,5,2,2,3,2],[3,3,7,6,9,2,5],[3,2,3,1,3,3,4],[1,8,4,8,9,7,4],[8,9,1,8,8,5,2]])

