def count_inversion(s):
	l=list(s)
	i,count=0,0
	while i<len(l)-1:
		if l[i]>l[i+1]:
			l[i],l[i+1]=l[i+1],l[i]
			count += 1
			if i!=0: i-=1
      		else: i+=1
	print (count,l)
	return l
    
if __name__ == '__main__':
	count_inversion((1, 2, 5, 3, 4, 7, 6))
	count_inversion((0, 1, 2, 3))
