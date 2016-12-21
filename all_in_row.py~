import re

new_data = []

def clean_data(new_data):
    final_data = []
    for i in new_data:
	final_data.append(i)
    new_data = []
    print new_data,final_data
    return final_data

def data_process(data):
    if len(data)==0:        
        return new_data
    for i in data:        
        if (type(i) == list and len(i) > 0):
            data_process(i)
        else:
            new_data.append(i)    
    return new_data
    
def checkio(data):
    global new_data
    new_data = []
    new_data = data_process(data)
    return new_data


l = [[[100]], [200, [300, 400, [6], 6, 6, 6], 7]]
print (checkio([1,[2,2,2],4]))
print (checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))

"""
print lst

for i in lst:
	print i,type(i)
"""

"""
lst = str(l)
lst = lst.split('[')
lst = str(lst)
lst = lst.split(']')
print type(lst)
print lst


for i in range(0,len(lst)):
	print lst(i)
"""

"""
s = [2,3,4,5]
t = s
print s
print t
s = []
print s
print t
"""

t = 0
print t

def test(n):
    t = n
    print t
    t = 0
    print t

test(10)
test(20)
