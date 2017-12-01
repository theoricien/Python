def ex_1():
    u = int(input("U(0): "))
    rang = int(input("U(x) maximum: "))
    un = u
    for i in range(1,rang+1):
        if u%2==0:
            un = u/2
        else:
            un = 3*un+1
        u = un
        print(i,un)

def ex_2():
    u = int(input("U(0): "))
    old = u
    rang = int(input("U(x) maximum: "))
    un = u
    for i in range(1,rang+1):
        if u%2==0:
            un = u/2
        else:
            un = (3*un+1)/2
        u = un
        print(i,un)
    etat = int(input("Etat attendu"))
    u = old
    i=1
    while True:
        if un == etat:
            print(i-1)
            break
        if u%2==0:
            un = u/2
        else:
            un = (3*un+1)/2
        u = un
        i+=1
