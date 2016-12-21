#!/usr/bin/python

f = open("output.txt","w")

i = [ i**2 for i in range(1,11)]

for n in i:
	f.write(str(n)+"\n")

f.close()
