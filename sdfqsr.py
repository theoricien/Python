def affiche(src):
    try:
        f = open(src,'r')
    except:
        raise ValueError("File seems to not existe in this directory.")
    s = "aa"
    while s != "":
        s = f.readline()
        print(s ,end = '')
    f.close()

def onliner_affiche(src):
    print(open(src,'r',encoding='utf-8').read())

def get_content_file(file):
    s = "aa"
    fin = ""
    while s != "":
        s = file.readline()
        fin += s
    return fin

def recopie(src, dst):
    try:
        sr = open(src,'r')
    except:
        raise ValueError("Source file seems to not existe in this directory.")
    try:
        dt = open(dst,'w+')
    except:
        raise ValueError("Destination file seems to not existe in this directory.")
    dt.write(get_content_file(sr))
    sr.close() ; dt.close()

def first_word(string):
    i = 0; s = ''
    for i in range(len(string)):
        if string[i] == ' ':
            return s
        s+=string[i]
    return s

def after_first_word(string):
    s = ''
    for i in range(index_first_word(string),len(string)):
         s+=string[i]
    return s

def index_first_word(string):
    i = 0; s = ''
    for i in range(len(string)):
        if string[i] == ' ':
            return i+1
        s+=string[i]
    return i

def word_without_quotes(string,n):
    s = ''
    for i in range(n,len(string)):
        if string[i] == ' ':
            return s
        if string[i] == '"' or string[i] == '\n':
            continue
        s+=string[i]
    return s
    
def pre_process(f_in, f_out, imported, included):
    # need to see if '#error' in f_in
    try:
        input_file = open(f_in, 'r')
    except:
        raise ValueError("Input file seems to not existe in this directory.")
    try:
        output_file = open(f_out, 'w+')
    except:
        input_file.close()
        raise ValueError("Output file seems to not existe in this directory.")
    s = 'aa'
    while s != "":
        s = input_file.readline()
        if first_word(s) == '#error':
            print(after_first_word(s), end='')
        elif first_word(s) == "#include":
            if word_without_quotes(s, index_first_word(s)) not in included:
                included += " " + word_without_quotes(s, index_first_word(s))
                pre_process( word_without_quotes(s, index_first_word(s)), 'output_include.txt' , imported, included)
        elif first_word(s) == "#import":
            if word_without_quotes(s, index_first_word(s)) not in imported:
                imported += " " + word_without_quotes(s, index_first_word(s))
            pre_process( word_without_quotes(s, index_first_word(s)), 'output_import.txt' , imported, included)
        else:
            print(s, end='')
            output_file.write(s)
    input_file.close() ; output_file.close()
    

pre_process('exemple.txt','test2.txt','')
