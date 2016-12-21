import itertools
def golf(c):
	l=[]
	for i in range(1,len(c)+1):
		for j in itertools.combinations(c,i):
			l.append(sum(j))
	return min([i for i in range(1,91) if i not in l])

if __name__ == '__main__':
	print golf([10,2,2,1])
	print golf([1,1,1,1])
	print golf([1,2,3,4,5])
