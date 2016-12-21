from random import randrange
def create_combo(x):
	r = []
	n = 1
	while True:
		tmp = []
		for i in range(x):
			tmp.append(randrange(1,x+1))
		t = sorted(tmp)
		if t not in r:
			r.append(t)
			print n,t
			n += 1
			
if __name__ == '__main__':
	create_combo(9)		
	
