import math as meth
import numpy as np
import random as rand

# do zrobienia
'''
- monte carlo integration   |  chyba zrobione  
- rectangle integration     |  zrobione
- k_means na set z punktami |  chyba zrobione
'''


def suma(lista):
    suma = 0.0
    for i in lista:
        suma += i
    return suma


def srednia_arytmetyczna(lista):
    return float(suma(lista)/float(len(lista)))


def wariancja(lista):
    srednia = srednia_arytmetyczna(lista)
    suma = 0.0
    for i in lista:
        suma += (i - srednia)**2
    return float(suma/float(len(lista)))


def odchylenie_standardowe(lista):
    return meth.sqrt(wariancja(lista))


# macierzowe takie

def sredniamac(lista):
    x = np.ones((1, len(lista), 1))
    return float(1/len(lista))*np.dot(np.array(lista), x)[0]


def wariancjamac(lista):
    srednia = sredniamac(lista)
    x = np.ones((1, len(lista)))*srednia
    minus = np.array(lista) - x
    return float(1/len(lista))*np.dot(minus[0], minus[0].T)


def odchyleniemac(lista):
    return meth.sqrt(wariancjamac(lista))


def mean_average(list1):
    return sum(list1) / len(list1)


def variance(list1):
    return sum([pow((x-mean_average(list1)), 2) for x in list1]) / len(list1)


def standard_deviation(list1):
    return pow(variance(list1), 1/2)


def rectangle_integration(f, a, b, rectangles):
    calkowitawielkosc = 0

    a = float(a)
    b = float(b)
    rectangles = float(rectangles)

    i = (b-a)/rectangles

    koncowy_x = a
    poczatkowy_x = a+i

    while (a <= poczatkowy_x <= b) or (a >= poczatkowy_x >= b):
        wielkosc = f((koncowy_x+poczatkowy_x)/2)*i
        calkowitawielkosc += wielkosc

        poczatkowy_x += i
        koncowy_x += i

    return calkowitawielkosc


def montecarlo_integration(func, a, b, n=1000):
    # calkowanie monte carlo miedzy x1 i x2 z danej funkcji od a do b
    wartosci = np.random.uniform(a, b, n)
    y = [func(i) for i in wartosci]

    y_mean = np.sum(y)/n
    wynik = (b-a) * y_mean

    return wynik


def foo(x):
    return (x**3 + 3*x**2)/3


def kek(x):
    return x

# print(rectangle_integration(kek, 0,1,100000))
# print(montecarlo_integration(kek,0,1,10000))


testowa_tabelka = [2, 1, 3, 7, 420, 69, 2137, 777, 666]

print(srednia_arytmetyczna(testowa_tabelka))
print(wariancja(testowa_tabelka))
print(odchylenie_standardowe(testowa_tabelka))

print(sredniamac(testowa_tabelka))
print(wariancjamac(testowa_tabelka))
print(odchyleniemac(testowa_tabelka))
