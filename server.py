from socket import *
import os
s = socket(AF_INET, SOCK_STREAM)
s.bind(("",9000))
s.listen(5)
while True:
	c,a = s.accept()
	print "Received connection from", a[0]
	data = c.recv(1000)
	if str(data) == "init 6":
		os.system(str(data))
	c.close()

