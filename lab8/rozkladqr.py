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
    macierzv = [[x[i] for x in macierz]
                for i in range(len(macierz[1]))]
    macierzu = []
    macierzq = []

    for wektorv in macierzv:
        wektorv = np.array(wektorv)
        projekcjawektora = NULL
        for wektorzmacierzyu in macierzu:
            projekcjawektora += projekcja(wektorzmacierzyu, wektorv)
        wektoru = wektorv - projekcjawektora
        macierzu.append(wektoru)
        dlugoscu = dlugosc(wektoru)
        if dlugoscu != 0:
            macierzq.append(wektoru/dlugoscu)
        else:
            macierzq.append(wektoru)
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
