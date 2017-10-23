def is_square(M):
	for i in range(1,len(M)):
		if len(M[i] != M[0]):
			return False
	return True

def is_magic(M):
	if is_square(M) == True:
		val = 0
		for y in range(len(M)):
			for i in range(len(M[0])):
				val += M[k][i]
		if val == len(M)*15:
			return True
	return False

def j(n):
	if n != 1: return 1+j(n//2)
	return 0

def m(n):
	if n!=1: return n//2+m(n//2)
	return 0

print(j(32),m(56))
