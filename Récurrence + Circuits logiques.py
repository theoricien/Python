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
		""" Comprendre les 2 questions d'avant:
	1):
	M(1) = 1 - 0
	M0(1) = 0
	M1(1)  = 1

	M(2) = 01 - 10 - 11
	M0(2) = 01
	M1(2) = 10 - 11

	M(3) = 010 - 011 - 101 - 110 - 111
	M0(3) = 010 - 011
	M1(3) = 101 - 110 -111

	M(4) = 0101 - 0111 - 0110 1010 - 1011 - 1101 - 
	1111 - 1110
	M0(4) = 0101 - 0111 - 0110
	M1(4) = 1010,1011,1101,1111,1110

	M(5) = 01010 - 10101 - 11111 - 11110 - 11101
	11011 - 10111 - 01111 - 01110 - 01101 - 10110
	- 11010 - 01011
	M0(5) = 01010 - 01111 - 01110 - 01101 - 01011
	M1(5) = 10101 - 11111 - 11110 - 11101 - 11011
	- 10111 - 10110 - 11010

	--------------------------------------------------------------------------------------------------------------------
	2): M_0(n) = M(n-2) car:
	M_0(n) commence forcément par '01'
	'01' est une chaine de longueur 2
	Du coup on a '01'.M(n-2) qui forme M_0(n)
	Donc M(n-2) possibilités

		M_1(n) = M(n-1) car:
	M_1(n) commence forcément par '1'
	len('1') = 1
	Du coup on a '1'.M(n-1) qui forme M_1(n)
	Donc M(n-1) possibilités
	----------------------------------------------------------------------------------------------------------------------
	On peut aussi introduire le système de bijection:
	A l'ensemble des mots de Dick de taille n qui ne comportent pas deux "0" consécutifs et qui commencent par "0"
	B l'ensemble des mots de Dick de taille n-2 qui ne comportent pas deux "0" consécutifs
	Ce qu'on veut montrer, c'est que A et B sont de même cardinal, et pour ça, il suffit de construire une bijection entre A et B.
	donc il faut : trouver une fonction A->B qui convient, montrer qu'elle est injective, et montrer qu'elle est surjective.

	Une fonction A->B = Pour tout a appartenant à A, il existe un unique b appartenant à B tel que f(a)=b

	   A  		     B
	{01 (a1) }	->	{b1}
	{01 (..) }	->	{..}
	{01 (an) }	->	{bn}
"""
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

def ex_12():
	"""
	1):
	2n^3 - 2n
	Initialisation: 
		Pour n_0 = 0, 2*1^3 - 2 = 2-2 = 0
		0 est un multiple de 3
		Donc vraie pour le rang n_0
	Hérédité:
		On suppose que la propriété est vraie au rang n
		On va le prouver au rang n+1
	Hypothèse de recurrence:
			P(n): 2n^3 - 2n est un multiple de 3
		Donc on a 2n^3 - 2n = 3k (k un relatif)
		On montre que 2(n+1)^3 - 2(n+1) = 3k'
		Et pour montrer ça, on utilise notre Hyptohèse de recurrence
		C'est à dire:
			2n^3 - 2n = 3k
		On décompose 2(n+1)^3 - 2(n+1) pour faire apparaitre 2n^3 - 2n dedans
		(n+1)^3 = (a+b)^3 = b^3 + 3a(b^2) + 3(a^2)b + a^3
				= 1 + 3n + 3n^2 + n^3
		* 2		= 2 + 6n + 6n^2 + 2n^3
		- 2(n+1)= (2n^3 + 6n^2 + 6n + 2) - 2n - 2
				= 2n^3 - 2n + (6n^2 + 6n)
				= P(n) + 6n^2 + 6n
				= P(n) = 3k' avec k' = 6n^2 + 6n qui est un multiplte de 3
	Conclusion:
		2n^3 - 2n = 3k avec k relatif pour tout n naturel différent de 0

	2):
	Il s'agit de trouver la classe de congruence de Z/3Z
	Wikipédia:
		Définition équivalente si n > 0 — Soit n un entier naturel non nul.
		Deux entiers a et b sont dits congrus modulo n si le reste de la division euclidienne de a par n est égal à celui de la division de b par n.
	Donc si pour X_n = 2n^3 - 2n:
		X_k % 3 = X_k' % 3 = 0
		6 % 3 = 0 % 3 = 0

	"""
	print("read the comment on the function")