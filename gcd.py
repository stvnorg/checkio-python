#!/usr/bin/python
import sys

def findGCD(m,n):
	r = m % n
	if r == 0:
		return n
	return findGCD(n,r)	

def gcd(*args):
	if len(args[0]) != 2:
		print "Usage: ./gcd.py <num1> <num2>"
		return 0
	m = int(args[0][0])
	n = int(args[0][1])
	print findGCD(m,n)	

if __name__ == '__main__':
	gcd(sys.argv[1:])


