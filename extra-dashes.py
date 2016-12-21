def checkio(data):
	count = 0
	n = ""
	for i in range(len(data)):
		if data[i] != '-' and data[i-1] == '-':
			count = 0
		if data[i] == '-' and count == 0:
			n += '-'
			count += 1
		elif data[i] == '-' and count == 1:
			pass
		else:
			n += data[i]
	return n

print checkio('I---like-python')
print checkio('I like python')
