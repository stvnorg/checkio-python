def median(data):
	lst = sorted(data)
	if len(lst) % 2 == 0:
		index_1 = len(lst)/2
		index_2 = index_1 - 1
		return (lst[index_1] + lst[index_2]) / 2
	else:
		return lst[len(lst)/2]

print median([34,5,57,2,1])
