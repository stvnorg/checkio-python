#!/usr/bin/python

lst_divisor = []

def is_prime(x):
	count = 0
	global lst_divisor 
	lst_divisor = []
	if (x<2):
		return False
	else:
		for i in range(x):
			if (x%(i+1)==0):
				count += 1
				lst_divisor.append(i+1)
			if count > 2:
				return False
		return True

#n = (2 ** 700000000) - 1

#print n


if (is_prime(1001)):
	print "Prime!"

print lst_divisor
