import string

def vect_sum2(x, y):
	return (x[0]+y[0],x[1]+y[1])

def vect_dim(v):
	return len(v)

def vect_sum(x,y):
	if vect_dim(x) != vect_dim(y): return False
	f = ()
	for i in range(vect_dim(x)):
		f += (x[i]+y[i],)
	return f

def find_alpha(s):
	for i in range(len(s)):
		if s[i].isalpha():
			return (i,s[i])
	return (-1)

def moyenne(L):
	m = 0
	for i in range(len(L)):
		m += L[i]
	return m/len(L)

my_pfc = ('pierre','feuille','cisea')

def f(s):
	global my_pfc
	return my_pfc.index(s)

def g(n):
	global my_pfc
	return my_pfc[n]

def new_periodic_list(l,p):
	f = []
	p_index = 0
	for i in range(l):
		if p_index == p:
			p_index = 0
		f += [p_index]
		p_index += 1
	return f

def padding(l, pattern):
	f = []
	for i in range(l):
		f += [pattern[i%len(pattern)]]
	return f

def est_triee(L):
	tmp = 0
	old_tmp = L[0]
	for i in range(len(L)):
		tmp = L[i]
		if old_tmp > tmp: return False
		old_tmp = tmp
	return True

def grouper(L):
	f = L
	lim = len(L)
	for i in range(1,lim):
		
	return f

print(grouper([1,1,2,2,3,3]))
