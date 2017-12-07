# un jeu
# se déplacer => une carte

from random import randint as ri

# MAIN

# CLASS
class enemy:
    # Fight
    health = 0
    attack = 0
    def __init__(self, curr_health, curr_atk):
        self.health = ri(5,7)*curr_health // 10
        self.attack = ri(1,6)
    def take_dmg(self, atk):
        self.health -= atk
    def dmg(self):
        return (ri(0,5)+self.attack)
    
# METHODS
def random_enemy():
    r = ri(0,3)
    if r == 1:
        return True
    return False

def found_potion():
    return ri(False,True)

def is_merchant():
    r = ri(0,10)
    if r == 1:
        return True
    return False

def take_random_list(L):
    res = []
    for i in range(ri(2,len(L))):
        res.append( L[ri(0,len(L)-1)] )
    return list(set(res))

def show_map(x,y, max_x, max_y):
    for i in range(max_y,0,-1):
        for j in range(1,max_x+1,1):
            if j == x and i == y:
                print('[X]',sep='',end='')
            else:
                print('[ ]',sep='',end='')
        print()

# INITIALIZAION
max_x = 5
max_y = 5

lieu = ["Mage Tower","Crypt","PGW 2017","Siphano convention","Graveyard","Haunted mansion","Amphi Informatique","Cours de Python","SNCF"]
stock_store = ["Wooden Sword","Wooden Helmet","Iron Sword","Iron Shield","Leather Armor"]
x = ri(1,max_x)
y = ri(1,max_y)
health = 100
health_max = health
attack = 5
nb_potions = 2
regen_potion = 30
charset = 'nswe'
move = 'a'
choice = ''
lvl = 0
gold = ri(30,50)

# MAIN LOOP
while True:
    while move not in charset:
        show_map(x,y,max_x,max_y)
        print("You are at {}".format(lieu[ri(0,len(lieu)-1)]))
        move = input('Move somewhere ? (n)orth , (w)est, (e)ast, (s)outh\nTake a (p)otion ?\n:')
        if move == 'n' and y < 5:
            y+=1
        elif move == 's' and y > 0:
            y-=1
        elif move == 'w' and x > 0:
            x-=1
        elif move == 'e' and x < 5:
            x+=1
        elif move == 'p':
            nb_potions -= 1
            health += 3*health_max//10
            if health > health_max:
                health = health_max
            print("You took a potion.\nYour current health: {}/{}\nYou have {} potions left.".format(health,health_max,nb_potions))
        else:
            continue
    if found_potion() == True:
        nb_potions +=1
        print("You found a health potion ! Great !\nYou have {} potions !".format(nb_potions))

    if is_merchant() == True:
        print('Merchant: Oh oh.. A visitor ! Let\'s check my store !\nYour gold: {}'.format(gold))
        L = take_random_list(stock_store)
        prices = []
        i = 0
        for i in range(len(L)):
            p = ri(20,70)
            print(i,'|',L[i],':',p)
            prices.append(p)
        print("What do you want to buy ? (q) to quit")
        c = -1
        while c not in range(len(L)):
            c = int(input("Choice: "))
            if c == 'q':
                break
            if prices[i] > gold:
                print("Too expensive for you !")
                continue
            gold -= prices[i]
            print("Now you have a {} !".format(L[i]))
        if L[i-2] == 'r' and L[0] == 'W':
            attack += 20
            print("New attack: {}".format(attack))
        elif L[i-2] == 'e' and L[0] == 'W':
            health += 20
            health_max += 20
        elif L[i-2] == 'r' and L[0] == 'I':
            attack += 30
        elif L[i-2] == 'l' and L[0] == 'I':
            health += 30
            health_max += 30
        elif L[i-2] == 'o' and L[0] == 'L':
            health += 20
            health_max += 20
        
    if random_enemy() == True:
        E = enemy(health_max, attack)
        print("Oh, an enemy !")
        while E.health > 0:
            # Fight
            print("Your health: {}\nYour attack: {}\n\nMonster health: {}\n".format(health, attack, E.health))
            choice = input("What do you want to do ?\n\t(A)ttack\n\t(P)otion\n\t(R)un\n:")
            if choice == 'A' or choice == 'a':
                E.take_dmg(ri(2,5)+attack)
                print("You deal {} damages ! He has {} HP left.".format(attack, E.health))
            elif choice == 'P' or choice == 'p':
                if nb_potions > 0:
                    nb_potions -= 1
                    health += 3*health_max//10
                    if health > health_max:
                        health = health_max
                else: continue
            elif choice == 'R' or choice == 'r':
                c = ri(0,1)
                if ri == 0:
                    print("You runned out")
                    break
                else:
                    print("You can't run out..")
                      
            if E.health < 0:
                print("You killed the monster !")
                break

            health -= E.dmg()
            print("The monster attacked you, you have {} HP left.".format(health))
            if health <= 0:
                print("You died, you loose.")
                exit()
        # monster beated
        attack += 5
        c = ri(5,20)
        health += c
        health_max += c
        lvl += 1
        gold += ri(10,20)
        print("LVL UP !\nHP: {}/{}\nAttack: {}\nGold: {}\nLVL: {}".format(health, health_max, attack, gold, lvl))
    else:
        print("There is no enemy here..")
    move = 'a'
        
        
