def ex_1():
	u = int(input("U(0): "))
	rang = int(input("U(x) maximum: "))
	un = u
	old_un = un
	for i in range(1,rang+1):
		if u%2==0:
			un = u/2
		else:
			un = 3*un+1
		u = un
		print(i,int(un))

	h = int(input("Valeur attendue: "))
	u = old_un
	un = old_un
	i=0
	while un != 2:
		if u%2==0:
			un = u/2
		else:
			un = 3*un+1
		u = un
		i+=1
	print("Resultat: {}".format(i))

def ex_2():
	u = int(input("U(0): "))
	rang = int(input("U(x) maximum: "))
	un = u
	old_un = un
	for i in range(1,rang):
		if u%2==0:
			un = u/2
		else:
			un = (3*un+1)/2
		u = un
		print(i,int(un))

	h = int(input("Valeur attendue: "))
	u = old_un
	un = old_un
	i=0
	while un != 2:
		if u%2==0:
			un = u/2
		else:
			un = (3*un+1)/2
		u = un
		i+=1
	print("Resultat: {}".format(i))

def ex_3():
	a = 1
	b = 1
	c = 3
	for i in range(21):
		print("M(",c-2,") =",a+b)
		old = a
		a = b
		b = old+b
		c += 1

def ex_4():
	u = int(input("U0: "))
	v = int(input("V0: "))
	fu = input("Formule de u(n+1) (vn = v ET un = u): ")
	fv = input("Formule de v(n+1) (vn = v ET un = u): ")
	un = lambda u,v: eval(fu)
	vn = lambda u,v: eval(fv)
	f = 0
	f2 = 0
	old_f = 0
	for i in range(1,9):
		if i == 1:
			f = un(u,v)
			f2 = vn(u,v)
		else:
			f = un(f,f2)
			f2 = vn(old_f,f2)
		print("Couple d'indice",i,":",f,"|",f2)
		old_f = f

def ex_5():
	ex_4()

def func_rec(a,b,c):
	if b > 0:
		return func_rec(a+1, b//5, [b%5,c])
	return c

def ex_6():
	print("Me fait pas chier, change la fonction fun_rec() avec tes trucs a toi, j'ai pas que ça a faire d'interpreter ta merde\nBisous <3")
	print( func_rec(int(input("a = ")), int(input("b = ")), []))

def ex_7():
	w0 = int(input("W0: "))
	w1 = int(input("W1: "))
	ff = input("Formule de w(j+2) (j = w0, k = w1): ")
	f = lambda j,k: eval(ff)
	old = 0
	old2 = 0
	for i in range(2,10):
		if i == 2:
			f1 = f(w0,w1)
		elif i == 3:
			f1 = f(w1,f1)
		else:
			f1 = f(old2,old)
		old2 = old
		old  = f1 
		print(i,'|',f1)

def pepe_is_illuminati(a,b,c,d):
	if a > d:
		return pepe_is_illuminati(a,b+1,c+d,c)
	print(b)


def ex_8():
	print("Fait pas chier, avant de tout mettre comme un tardos tu vas dans la fonction juste au dessus qui se nomme pepe_is_illuminati() et tu mets les valeurs qui changent, flemme de faire un super systeme chelou, la bize.")
	a = int(input("a = "))
	b = int(input("b = "))
	c = int(input("c = "))
	d = int(input("d = "))
	pepe_is_illuminati(a,b,c,d)

def pgcd(a,b):
	if b==0:
		return a
	else:
		r=a%b
		return pgcd(b,r)

def ppcm(a,b):
	if (a==0) or (b==0):
		return 0
	else:
		return (a*b)//pgcd(a,b)

def ex_9():
	test = int(input("(1) ppcm(m,n) = X , m+n = Y\n(2) ppcm(m,n) = X , m*n = Y\n:"))
	a = int(input("ppcm(m,n) = "))
	b = int(input("m +/* n = "))
	if test == 1:
		for n in range(b):
			for m in range(a):
				if ppcm(m,n) == a and m+n == b:
					print(m,n)
					return
	else:
		for n in range(b):
			for m in range(a):
				if ppcm(m,n) == a and m*n == b:
					print(m,n)
					return
def ex_11():
	print("Rappels:\nA ou B = A + B\nA et B = A * B\nnon A ou B = (1-A) + B\nA - B = A*(1-B)\nA xor B = A + B - 2*A*B")