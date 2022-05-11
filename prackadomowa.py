import math as meth
import numpy as np
import random as rand

# do zrobienia
'''
- monte carlo integration   |  chyba zrobione  
- rectangle integration     |
- k_means na set z punktami |
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
    x = np.ones((1,len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista), x)[0]

def wariancjamac(lista):
    srednia = sredniamac(lista)
    x = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - x
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchyleniemac(lista):
    return meth.sqrt(wariancjamac(lista))


def mean_average(list1):
    return sum(list1) / len(list1)

def variance(list1):
    return sum([pow((x-mean_average(list1)), 2) for x in list1]) / len(list1)

def standard_deviation(list1):
    return pow(variance(list1), 1/2)




def rectint(f,a,b,rectangles):
    cumulative_area=0

    a=float(a)
    b=float(b)
    rectangles=float(rectangles)

    i=(b-a)/rectangles

    trailing_x=a
    leading_x=a+i

    while (a<=leading_x<=b) or (a>=leading_x>=b):
        area=f((trailing_x+leading_x)/2)*i
        cumulative_area+=area

        leading_x+=i
        trailing_x+=i

    return cumulative_area


def mc_integrate(func, a, b, n = 1000):
    # Monte Carlo integration between x1 and x2 of given function from a to b
    
    vals = np.random.uniform(a, b, n)
    y = [func(val) for val in vals]
    
    y_mean = np.sum(y)/n
    integ = (b-a) * y_mean
    
    return integ


def foo(x):
    # return x**2 + 2*x   # to jest funkcja
    return (x**3+ 3*x**2)/3   # to jest całka powyzszej


print(rectint(foo, 4,7,100000))
print(mc_integrate(foo,4,7,10000))
