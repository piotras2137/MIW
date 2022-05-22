from calendar import c
import math as meth 
import numpy as np
import random 

dane = [ [float(j) for j in line.strip('\n').split(' ')]  for line in open('australian.dat', 'r').readlines()]
 
 
def euklides(e1, e2):
    wynik = 0 
    for i in range(0,len(e1)-1, 1):
        wynik+=meth.pow(e1[i]-e2[i],2) 
    return meth.sqrt(wynik)


X = [i/i for i in range(1,16,1)]


def funkcja(x, lista):
    return [[i[-1],euklides(i,x)] for i in lista]


def slownikzfunckji(tupl):
    slownik = {}

    for i in tupl:
        if i[0] not in slownik.keys():
            slownik[int(i[0])] = [i[1]]
        else:
            slownik[int(i[0])].append(i[1])

    return slownik

dicton = slownikzfunckji(funkcja(X,dane))

for i in range(0,5,1):
    print(dicton[0][i])


def knajblizszychsasiadow(slownik,k):
    wynik = {}

    for i in slownik.keys():
        z = slownik[i]
        z.sort()
        z = z[:k]
        wynik[i] = sum(z) 

    return wynik

print(knajblizszychsasiadow(dicton,5))


# do domu jest :
'''
zrobic metryke euklidesowa w oparciu o wektor i dzialania na wektorze, 
chodzi o matematyczny wektor i dzialania na nim 


łącząc wszystkie funkcje ze soba trzeba zrobic co bierze, x, k i liste i zwraca decyzje
'''

def  combofunkcja(x, k, lista):
    najblizszi = knajblizszychsasiadow(slownikzfunckji(funkcja(x,lista)),k)
    return min(najblizszi, key=najblizszi.get)

print(combofunkcja(X,5, dane))


def prackadomowa(x, k, lista):
    slownik = {}
    wynik = {}

    for i in [[i[-1],euklideswektor(i,x)] for i in lista]:
        if i[0] not in slownik.keys():
            slownik[int(i[0])] = [i[1]]
        else:
            slownik[int(i[0])].append(i[1])

    for i in slownik.keys():
        z = slownik[i]
        z.sort()
        z = z[:k]
        wynik[i] = sum(z) 

    return min(wynik,key=wynik.get)
    


def euklideswektor(l1, l2):
    v1 = np.array(l1[:-1])
    v2 = np.array(l2[:-1])
    sub = v1 - v2
    return meth.sqrt(np.dot(sub,sub))


print(prackadomowa(X,5,dane))



def kolor(x, kolor):
    x[-1] = kolor

def kolorowanie(dane):
    for i in dane:
        kolor(i,random.randint(0,1))

    slownik = {}
    srodki = {}

    for i in range(0,10,1):
        print(srodki)
        for i in dane:
            if int(i[-1]) not in slownik.keys():
                slownik[int(i[-1])] = [i]
            else:
                slownik[int(i[-1])].append(i)

        x = list(slownik.keys())

        for i in x:
            srodki[i]=[1e500, []]

        for i in list(slownik.keys()):
            for j in slownik[i]:
                suma = 0
                for k in slownik[i]:
                    suma += euklideswektor(j,k)

                if suma < srodki[i][0]:
                    srodki[i][0] = suma
                    srodki[i][1] = j

        for i in dane:
            letter = -1
            val = 1e500
            for j in list(slownik.keys()):
                if euklideswektor(srodki[j][1],i) < val:
                    letter = j 
                    val = euklideswektor(srodki[j][1],i)
            
            i[-1] = letter
        
        dupa = slownikzfunckji(dane)
        print('wartosc 0: ', len(dupa[0]), 'wartosc 1: ', len(dupa[1]))
    
    return dane



w = kolorowanie(dane)
plik2 = open('kek.txt', 'w')
for i in w:
    s = str(i).strip('[').strip(']') 
    s = s + '\n'
    plik2.write(s)
plik2.close()

# kazdemu nadaje za pomoca randoma albo 0 albo 1 
# od kazdej kropki czarnej licze odleglosc do kazdej kropki czarnej i tak dla wszystkich 
# biore po kolei kazda z kropek i licze odleglosci do srodkow 
# ustawiam jej kolor na ten co jest blizej 
# znowu licze srodek masy tego bytu 
# robimy tak dlugo az zadna nie zmieni koloru albo minie 10 iteracji