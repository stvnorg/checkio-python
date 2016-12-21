from collections import deque

def letter_queue(l):
	r = deque()
	for i in l:
		if "PUSH" in i: r.append(i.split(' ')[1])
		if "POP" in i:
			try:
				r.popleft()
			except:
				pass
	print "".join(r)

if __name__ == '__main__':
	letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])
	letter_queue(["POP","POP"])
	letter_queue(["PUSH H", "PUSH I"])
	letter_queue([])

	
