# my imports
from fr_dic import fr_dic
from random import randint
from unicodedata import normalize

# global vars


# my funcs
def rm_space(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] != ' ':
            new_s += s[i]
    return new_s

def rand_word():
    global fr_dic
    return fr_dic[randint(0,len(fr_dic))]

def start(m):
    l = []
    for i in range(len(m)):
        if i == 0 or i == len(m)-1:
            l += m[i]
        else:
            l += '_'
    return l
        
def word_to_list(m):
    l = []
    for i in range(len(m)):
        l.append(m[i])
    return l

def list_to_word(L):
    s = ''
    for i in range(len(L)):
        s += L[i] + ' '
    return s

def update(L,word,char):
    b = False
    for i in range(len(L)):
        if to_ascii(char) == to_ascii(word[i]) and to_ascii(word[i]) != L[i]:
            L[i] = word[i]
            b = True
    return b

def to_ascii(s):
    return normalize('NFKD',s).encode('ascii','ignore').decode('ascii')

def play():
    my_word = rand_word()
    secret_word = list_to_word(start(my_word))
    lives = 10
    char_input = ''
    print(secret_word)
    print('Hello human, what\'s your choice ?' ,end='')
    while lives > 0 and my_word != rm_space(secret_word):
        char_input = str(input())
        s = word_to_list(rm_space(secret_word))
        if update(s,my_word,char_input) == False:
            print('Oh no.. you loose 1 live')
            lives -= 1
        else:
            print('Oh damn !')
        print('Lives left:',lives)
        secret_word = list_to_word(s)
        print(secret_word, 'The choice: ', end='')
        #print(rm_space(secret_word),my_word,rm_space(secret_word)==my_word)
    if my_word == rm_space(secret_word):
        print('GG MEN')
    else :
        print('Oh.. so uh... you loose.. LEL NUB XDDD')

def play_bot():
    def search(l,s_w):
            # take list w/ index and char of s_w, and check in fr_dic
            # and, cmp the letter the more used
        f = [c for c in s_w if c.isalpha]
        s = [s_w.index(f[i]) for i in range(len(s_w))]
        for k in range(len(s_w)):
            for i in range(len(l)):
                if f[k] != l[i][s[k]]:
                    l.remove(l[i])
        print('ok')
    def choose_char(l):
        charset = "azertyuiopqsdfghjklmwxcvbn"
        ecx = 0
        old_ecx = [0,0]
        for i in range(len(charset)):
            s = list_to_word(l[i])
            for j in range(len(s)):
               if charset[i] == s[j]:
                   ecx += 1
            if old_ecx[0] < ecx:
               old_ecx = [ecx,i]
        return old_ecx[1]
    r_w = rand_word()
    s_w = list_to_word(start(r_w))
    list_w = [w for w in fr_dic if w[0]==r_w[0] and w[-1]==r_w[-1] and len(w)==len(r_w)] # list that contain all the possible word
    lives = 10
    print('the word is:', r_w)
    while lives > 0 and r_w != rm_space(s_w):
        search(list_w,s_w)
        c = choose_char(list_w)
               
        s = word_to_list(rm_space(secret_word))
        update(s,r_w,c)
        s_w = list_to_word(s)
               
        lives-=1
        print(c,r_w,s_w,lives)
# main loop
play_bot()
