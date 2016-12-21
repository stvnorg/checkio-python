def golf(x):
	n=0
	for i in range(x+1,98690):
		for j in range(1,98690):
			if i%j==0: n+=1
			if n>2: n=0;break
		if n==2 and str(i)==str(i)[::-1]: return i

if __name__ == '__main__':
	print (golf(2))
	print (golf(13))
	print (golf(101))
	print (golf(98688))
