#!/usr/bin/python

import math;
import random;
import time;

print "Hi, what is your name"
name = raw_input()
print "O Hi "+name

mylist = ['test',123,4.5,'steven']

for a in mylist:
	print a

for a in mylist:
	print (str(a).count('e'))

myCC = ''

for x in range(0,4):
	myCC += str(random.randrange(1000,10000,1))
	myCC += " "

print "Hi Mr.%s, your Credit Card number is %s" % (name, myCC)

i = 0
while (i < 10):
	i += 1
	if i == 5:
		continue
	print i
	
for n in range (10,20):
	if n == 15:
		break
	print n

mylist.insert(1,'newdata')

print min(mylist)

mytuple1 = (3,'tuple',6.0,'fruit')

mytuple2 = ('grape',100,'wine',1.2)

mytuple3 = mytuple1 + mytuple2

print mytuple3[3:5]
print len(mytuple3)

mydict = {'name':'steven','age':29,'sex':'male'}

print (mydict['age'])
mydict['name'] = 'Steven'
print str(mydict)

mydict.clear()
print mydict

ticks = time.time()
print ticks

z = 0
while z < 10:
	print z
	z+=1
