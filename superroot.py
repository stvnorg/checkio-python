def super_root(x):
	x = float(x)
	n = 0.01
	j = 0.99
	while j <= 2.01:
		if j**j == x: print (j)
		#print j
		j += n

if __name__ == "__main__":
	super_root(4)
 
