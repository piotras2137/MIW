import numpy as np 
import math as meth


def Srednia(lista):
    x = np.ones((1,len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista), x)[0][0]

def wariancjamac(lista):
    srednia = Srednia(lista)
    x = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - x
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchyleniemac(lista):
    return meth.sqrt(wariancjamac(lista))


testowa_tabelka = [2,1,3,7, 420, 69, 2137, 777, 666]

print(Srednia(testowa_tabelka))
print(wariancjamac(testowa_tabelka))
print(odchyleniemac(testowa_tabelka))








'''
punkty wczytujesz z pliku
'''

def funkcja(x, y):
    xtrans = x.transpose()
    return (xtrans*x)**1*(xtrans*y)