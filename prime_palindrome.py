def is_palindrome(n):
	str_n = str(n)
        n_palindrome = ""
        for i in range(len(str_n)-1,-1,-1):
		n_palindrome += str_n[i]
	if str_n == n_palindrome:
		return True


def is_prime(n):
	count = 0
	for i in range(1,n+1):
		if (n%i==0):
			count += 1
	if count == 2:
		return True


def prime_palindrome(n):
        condition = True
	m = n
	while condition:
		if is_prime(m) and is_palindrome(m):
			condition = False
		else:
			m += 1
	return m

m = 1000
print (prime_palindrome(m))

"""
if is_palindrome(n) and is_prime(n):
	print "Prime Palindrome"
"""
