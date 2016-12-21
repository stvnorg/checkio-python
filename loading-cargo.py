import math

def total_weight(lst):
    total = 0
    for i in lst:
        total += i
    return total

def check_exist(sequence, lst):
    check_bool = False
    if len(lst) == 0:
        return False
    for i in range(0,len(lst)):        
        if lst[i] in sequence:
            check_bool = True
        else:
            check_bool = False
    return check_bool

def count(sequence,item):
    total = 0
    n = 0
    if (type(item) == list):
        while n < len(sequence):            
            if sequence[n:n+len(item)] == item:                
                n += len(item)                
                total += 1
            else:
                n += 1
    else:
        for i in range(0,len(sequence)):
            if sequence[i] == item:
                total += 1            
    return total

def lowest_possible(lst,weight_bal,index_range):
    l = lst
    lst = sorted(lst)
#   lst.reverse()
    weight_list = []        
    x = weight_bal
    i_range = index_range 
    for i in range(i_range,len(lst)):
	x -= lst[i]
#	print x          
        if x > 0 and x in lst:
            weight_list.append(lst[i])
            break
        if x > 0 and x not in lst:
            weight_list.append(lst[i])
	elif x == 0:
	    weight_list.append(lst[i])
	    break
        else:
            weight_list = []
    i_range += 1
    if check_exist(lst,weight_list):
	return True
    elif check_exist(lst,weight_list) == False and i_range == len(lst)-1:
        return False
    else:
	lowest_possible(l,weight_bal,i_range)
                
def checkio(data):
    weight_balance = 0
    lowest_difference = 0    
    if len(data) == 1:
        lowest_difference = data[0]
    elif len(data) == 2:
        lowest_difference = abs(data[0] - data[1])        
    elif len(data) > 2:        
        weight_balance = int(total_weight(data) / 2)       
	for i in range(weight_balance,0,-1):
	        if lowest_possible(data,i,0):
#			print i
			return abs((total_weight(data)-i) - i)
    else:
        pass
    return lowest_difference

print checkio([10, 10])
print checkio([10])
print checkio([5, 8, 13, 27, 14])
print checkio([5, 5, 6, 5])
print checkio([12, 30, 30, 32, 42, 49])
print checkio([1, 1, 1, 3])
