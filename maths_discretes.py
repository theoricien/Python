import re

#Applications modulaires - deux variables
def ex_1():
	print("Reponse:",[(nb_x*x + nb_y*y) % mod for nb_x in [int(input("Coeff de x: "))] for nb_y in [int(input("Coeff de y: "))] for mod in [int(input("Modulo: "))] for y in range(int(input("Nb de lignes: "))) for x in range(int(input("Nb de colonnes: ")))],end='')

#Valeurs d'une fonction trinôme en calcul modulaire - Trous de trinôme 
def ex_2():
	#trinome => 3 values + 1 mod
	print("Reponse:",[(a*x**2+b*x+c)%m for a in [int(input("Coeff de x²: "))] for b in [int(input("Coeff de x: "))] for c in [int(input("Nombre apres x: "))] for m in [int(input("Modulo: "))] for x in range(m)])

#Valeurs d'une fonction polynomiale en calcul modulaire - Trous de polynôme 
def ex_3():
	#polynome => x values + 1 mod, so use lambda x
	# demande la formule : (x**8 − 4x**5 + x − 3) % 5
	# on prend le dernier terme: 5 et on fait un for avec, et x prendra les valeurs
	formule = input("formule (exemple: '(x**8 - 4*x**5 + x - 3) % 5' ): ")
	g = lambda x: eval(formule) # Attention, n'utilisez eval() que quand vous savez ce que vous faites, #SecuriteInformatique
	print("Reponse:",[g(t) for t in range(int(re.findall(r'\d+', formule)[-1]))])

#Image, image réciproque en calcul modulaire - Eléments par polynôme - niveau 1 
def ex_4():
	formule = input("formule (exemple: '(x**8 - 4*x**5 + x - 3) % 5' ): ")
	final = int(input("Dernier chiffre du premier ensemble: "))+1
	g = lambda x: eval(formule)
	tab = [g(t) for t in range(final)]
	print("Reponses:\n\t(1) Au choix (si []: -1): ",[tab[i] for i in range(len(tab)) if tab.count(i)>1],"\n\t(2): -1\n\t(3) Au choix (si []: -1): ",[i for i in range(len(tab)) if i not in tab],"\n\t(4):-1",sep='')

def ex_5():
	formule = input("formule (exemple: '(x**8 - 4*x**5 + x - 3) % 5' ): ")
	final = int(input("Dernier chiffre du premier ensemble: "))+1
	g = lambda x: eval(formule)
	tab = [g(t) for t in range(final)]
	print([i for i in range(len(tab))],"\n",tab,sep='')
	print("Cardinal: ",len(set(tab)),"\nImage de f:",set(tab),sep='')

def ex_6():
	formule = input("formule (exemple: '5**789' ): ")
	m = int(input("Modulo: "))
	g = eval(formule)
	print(g%m)

def ex_7():
	formule = input("formule (exemple: 'x**789' ): ")
	m = int(input("Modulo: "))
	g = lambda x: eval(formule)
	print([g(t)%m for t in range(m)])

def ex_10():
	formule = input("formule (exemple: '5*x**2 + 5' ): ")
	res = int(input("resultat attendu: "))
	m = int(input("Modulo: "))
	g = lambda x: eval(formule)
	for i in range(m):
		if g(i)%m==res:
			print(i)
			break

def ex_11():
	somme = int(input("Somme attendu: "))
	produit = int(input("Produit attendu: "))
	m = int(input("Modulo: "))
	for i in range(500):
		for j in range(500):
			if (j+i)%m==somme and (j*i)%m==produit:
				print(i,j)
				return None
				
def eudoxe(a,b,index):
	if a==0:
		print("a",index-1,": ",a,"   b",index-1,": ",b,sep='')
		return index
	else:
		u = b//a
		print("a",index-1,": ",a,"   b",index-1,": ",b,sep='')
		return eudoxe(b - u * a, a,index+1)

def ex_12():
	a = int(input("a: "))
	b = int(input("b: "))
	print("Nb de recursions:",eudoxe(a,b,1))

# don't work
def ex_13():
	nb_b = int(input("Nombre de boites: "))
	nb_c = int(input("Nombre de caisses: "))
	print(nb_b//nb_c," caisses pleines\n",nb_b%nb_c," boites restantes",sep='')

def pgcd(m,n):
	while m%n != 0:
		m, n = n, m%n
	return n

def ex_14():
	print("Forme de l'exo:\n\t(1)pgcd(m,n) = X , m+n = Y\n\t(2)pgcd(m,n) = X , m*n = Y\n\t(3)pgcd(m,n) =/= pgcd(Xm,n)")
	i = int(input())
	if i == 1:
		a = int(input("Resultat du PGCD: "))
		b = int(input("Somme de m et n: "))
		for m in range(1,b,1):
			for n in range(1,b,1):
				if pgcd(m,n) == a and m+n==b:
					print(m,n)
					return None
	elif i == 2:
		a = int(input("Resultat du PGCD: "))
		b = int(input("Produit de m et n: "))
		for n in range(1,b):
			if pgcd(a,n) == a and a*n==b:
				print(a,n)
				return None
		#Si ca ne marche pas, essayez cette algo, du pure bruteforce mais bon faut employer les gros moyens
		#a = int(input("Resultat du PGCD: "))
		#b = int(input("Produit de m et n: "))
		#for m in range(1,b):
		#	for n in range(1,b):
		#		if pgcd(m,n) == a and m*n==b:
		#			print(m,n)
		#			return None
	else:
		a = input("Mettez la lettre qui a change de coeff dans l'equation:")
		b = input("(1) =\n(2) =/=\n:")
		if a == 'm' and b == '1':
			print("Quand coefficient ne divise pas n\nSuffisante")
		elif a == 'm' and b == '2':
			print("Quand coefficient divise n\nNecessaire")
		elif a == 'n' and b == '1':
			print("Quand coefficient ne divise pas m\nSuffisante")
		else:
			print("Quand coefficient divise m\nNecessaire")
		return None

ex_14()