# fast finger program
from time import time
from random import randint

# consts
lim = 60
dic = ["un","deux","trois","maison","bleu","rouge","une","voiture","liste","tortue","chat","animal","normal","anormal"
,"bloc","def","class","for i in range","while"]

counter = 0
t = time()
while(time()-t <= lim):
	i = dic[randint(0,len(dic)-1)]
	o = input('Word: '+i+'\n')
	if i==o:
		counter += 1
print(str(counter * lim//60) + ' WPM')