import math as meth
import numpy as np


def slownikzfunckji(tupl):
    slownik = {}

    for i in tupl:
        if i[0] not in slownik.keys():
            slownik[int(i[0])] = [i[1]]
        else:
            slownik[int(i[0])].append(i[1])

    return slownik

def euklides(l1, l2):
    v1 = np.array(l1[:-1])
    v2 = np.array(l2[:-1])
    sub = v1 - v2
    return meth.sqrt(np.dot(sub,sub))


def slownik(dane):
    slownik = {}
    for i in dane:
        if int(i[-1]) not in slownik.keys():
            slownik[int(i[-1])] = [i]
        else:
            slownik[int(i[-1])].append(i)
    return slownik

def zmiana_koloru(srodki, dane):
    for i in dane:
        letter = -1
        val = 1e500
        for j in list(slownik.keys()):
            if euklides(srodki[j][1],i) < val:
                letter = j 
                val = euklides(srodki[j][1],i)
                
        i[-1] = letter


def kolorowanie(dane):
    slownik = slownik(dane)
    srodki = {}
    for i in range(0, 10 ,1):
        x = list(slownik.keys())

        for i in x:
            srodki[i]=[1e500, []]

        for i in list(slownik.keys()):
            for j in slownik[i]:
                suma = 0
                for k in slownik[i]:
                    suma += euklides(j,k)

                if suma < srodki[i][0]:
                    srodki[i][0] = suma
                    srodki[i][1] = j

        zmiana_koloru(srodki, dane)

        dupa = slownikzfunckji(dane)
        print('wartosc 0: ', len(dupa[0]), 'wartosc 1: ', len(dupa[1]))
    return dane

