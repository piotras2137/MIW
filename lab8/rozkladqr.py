from asyncio.windows_events import NULL
import numpy as np
import math as m


def dlugosc(macierz):
    return m.sqrt(np.dot(macierz.T, macierz))


def zaookroglenie(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            macierz[i][j] = round(macierz[i][j], 3)
    return macierz


def projekcja(u, v):
    licznik = np.dot(u.T, v)
    mianownik = np.dot(u.T, u)
    if mianownik != 0:
        return licznik/mianownik*u
    else:
        return mianownik


def rozkladqr(macierz):
    macierzv = macierz.T
    macierzu = []
    macierzq = []
    for wektorv in macierzv:
        suma = 0
        for wektoru in macierzu:
            suma += projekcja(wektoru, wektorv)
        wektoru = wektorv - suma
        macierzu.append(wektoru)
        if dlugosc(wektoru) == 1:
            wektore = wektoru
        else:
            wektore = wektoru * (1 / dlugosc(wektoru))
        macierzq.append(wektore)
    Q = np.array(macierzq).T
    R = np.dot(Q.T, macierz)
    return Q, R


macierz_testowa = np.array([
    [2, 0, 1],
    [0, 1, 1],
    [4, 1, 1],
    [1, 2, 1],
])

Q, R = rozkladqr(macierz_testowa)
print(Q)
print(R)
