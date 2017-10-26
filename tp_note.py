from random import randint

curr_year = 2017

def exo1():
    global curr_year
    age = int(input("Quel est ton, humain? "))
    print("Tu est né.e en ",curr_year - age,".",sep='')

def exo2():
    counter = 0
    d1 = 1
    d2 = 2
    # we don't know the limit of the loop
    while d1 != d2:
        counter += 1
        d1 = randint(1,6)
        d2 = randint(1,6)
        print("essai",counter,": d1 =",d1,", d2 =",d2,sep=' ',end='\n')
    print("gagné! Nombres d'essai :",counter)

def tapis_A(n,m):
    for i in range(n):
        for i in range(m):
            print("*",sep='',end='')
        print('') # line feed

def tapis_B(n,m):
    i = m # nb of columns
    for k in range(0,n//2):
        i -= 2
        print('#'*k,'*','#'*i,'*','#'*k,sep='',end='')
        print('')
    for k in range(n//2):
        print('#'*(m//2 - 1),'**','#'*(m//2 - 1),sep='',end='')
        print('')
                  
def tapis_C(n,m):
    nb_hashtags = m//4
    nb_stars = m//2 - m//4 # if m = 10, nb_stars = 3
    old_st = nb_stars
    old_ht = nb_hashtags
    for i in range(n):
        for i in range(m//2):
            if old_st>0:
                old_st -= 1 ; print('**',sep='',end='')
            if old_ht>0:
                old_ht -= 1; print('##',sep='',end='')
            if old_ht==0 and old_st==0:
                break;
        print('')
        old_st = nb_stars
        old_ht = nb_hashtags
    
def diff_crypto(c1, c2):
    charset = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return charset[(charset.index(c1)-charset.index(c2))%len(charset)]

def encrypt(m,k):
    def new_k(m,k):
        i=0
        n_k=k
        while(len(m)!=len(n_k)):
            n_k+=k[i%len(k)]
            i+=1
        return n_k
    n_k=new_k(m,k)
    s=""
    for i in range(len(m)):
        s+=diff_crypto(m[i],n_k[i])
    return s

