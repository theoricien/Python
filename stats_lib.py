from math import *

def ask_array ():
    size = int(input("Number of columns:"))
    print()
    T = [[[0] for j in range(2)] for i in range(size)]
    for i in range(size):
        T[i][0] = float(input("Value at column %d:" % (i)))
        T[i][1] = float(input("Effectifs at column %d:" % (i)))
        print()
    return T

def ask_regression ():
    size = int(input("Number of columns:"))
    print()
    T = [[0] for i in range(size)]
    for i in range(size):
        T[i] = float(input("Value at column %d:" % (i)))
    return T

def effectif_total (T):
    return sum([T[i][1] for i in range(len(T))])

def r_effectif_total (T):
    return len(T)

def moyenne (T):
    return sum([T[i][0] * T[i][1] for i in range(len(T))])/effectif_total(T)

def r_moyenne (T):
    return sum(T)/r_effectif_total(T)

def quartile(T,i):
    T_ = []
    for y in range(len(T)):
        for x in range(int(T[y][1])):
            T_ += [T[y][0]]
    return T_[ceil(len(T_)*((i%4)/4))]

def mediane (T):
    T_ = []
    for y in range(len(T)):
        for x in range(int(T[y][1])):
            T_ += [T[y][0]]
    return T_[ceil(len(T_)*1/2)]

def decile (T):
    T_ = []
    for y in range(len(T)):
        for x in range(int(T[y][1])):
            T_ += [T[y][0]]
    for i in range(1,10):
        print('\td%d: %.2f' % (i,T_[ceil(len(T_)*i/10)] ))

def freq (n,N):
    return n/N

def freq_cum (T,i,j):
    F = [freq(T[x][1],effectif_total(T)) for x in range(i,j)]
    for i in range(len(F)):
        print('\tF%d: ' % (i) + str(sum(F[:i+1])))

def variance (T):
    T_ = []
    for y in range(len(T)):
        for x in range(int(T[y][1])):
            T_ += [T[y][0]]
    m = moyenne(T)
    t = effectif_total(T)
    return sum([abs((T_[x] - m)**2)/(t - 1) for x in range(len(T_))])

def r_variance (T):
    m = r_moyenne(T)
    t = r_effectif_total(T)
    return sum([(T[x] - m)**2 for x in range(len(T))])/(t-1)

def ecart_type (T):
    return sqrt(variance(T))

def r_ecart_type (T):
    return sqrt(r_variance(T))

def cov (X, Y):
    if len(X) == len(Y):
        mx = r_moyenne(X)
        my = r_moyenne(Y)
        return sum([((X[i] - mx)*(Y[i] - my)) for i in range(len(X))])/r_effectif_total(X)
    return False

def r_droite (X, Y):
    b = cov(X,Y)/r_variance(X)
    a = r_moyenne(Y) - b * r_moyenne(X)
    print('\tf(x) = %.2f + %.2fx' % (a,b))

def give_all (T,deciles=False):
    print('-------------------')
    print('Effectif total: %d' % (effectif_total(T)))
    print('Moyenne: %.2f' % (moyenne(T)))
    print('Quartile 1: %.2f' % (quartile(T,1)))
    print('Mediane: %.2f' % (mediane(T)))
    print('Quartile 3: %.2f' % (quartile(T,3)))
    if deciles == True:
        print('Déciles:')
        decile(T)
    print('Fréquence cumulée:')
    freq_cum(T,0,len(T))
    print('Fréquences:')
    for i in range(len(T)):
        print('\t%.2f%% at [%.2f,%.2f]' % (freq(T[i][1],effectif_total(T))*100, T[i][0], T[i][1]))
    print('Variance: %.2f' % (variance(T)))
    print('Ecart Type: %.2f' % (ecart_type(T)))
    print('-------------------')

def r_give_all (X,Y):
    print('-------------------')
    print('Effectif total de X: %d' % (r_effectif_total(X)))
    print('Effectif total de Y: %d' % (r_effectif_total(Y)))
    print('Moyenne de X: %.2f' % (r_moyenne(X)))
    print('Moyenne de Y: %.2f' % (r_moyenne(Y)))
    print('Variance de X: %.2f' % (r_variance(X)))
    print('Variance de Y: %.2f' % (r_variance(Y)))
    print('Ecart Type de X: %.2f' % (r_ecart_type(X)))
    print('Ecart Type de Y: %.2f' % (r_ecart_type(Y)))
    print('Covariance: %.2f' % (cov(X,Y)))
    print('Droite de régression de X en fonction de Y:')
    r_droite(X,Y)
    print('Droite de régression de Y en fonction de X:')
    r_droite(Y,X)
    print('-------------------')

def classic (d=False):
    T = ask_array()
    give_all(T,d)

def regr ():
    X = ask_regression()
    Y = ask_regression()
    r_give_all(X,Y)

def main():
    print('a')
    
if __name__ == '__main__':
    main()
