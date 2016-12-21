from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",9000))
#s.send("GET /index.html HTTP/1.0\n\n")
s.send("init 6")
data = s.recv(10000)
print (str(data))
s.close()
