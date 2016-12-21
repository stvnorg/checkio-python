#!/usr/bin/python

# count the occurence of an item/items in a sequence
# steven stevanus -- stvn.org@gmail.com, stevenstevanus@gmail.com

def count(sequence,item):
    total = 0
    i = 0
    if (type(item) == list):
	while i < len(sequence):
		if sequence[i:i+len(item)] == item:
			total += 1
			i += len(item)
		else:
			i += 1	
    else:
        for i in range(0,len(sequence)):
            if sequence[i] == item:
                total += 1
            
    return total

print count([1,1,1,2,1,1,1],["a"])
