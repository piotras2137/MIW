import math as m
import numpy as np


def dlugosc(macierz):
    return m.sqrt(np.dot(macierz.T, macierz))


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


def macierz_k(macierz):
    macierzq, r = rozkladqr(macierz)
    macierzk = np.dot(np.dot(macierzq.T, macierz), macierzq)
    return macierzk


def wartosciwlasne(macierz):
    macierzwartosciwlasnych = macierz
    while (np.diag(macierzwartosciwlasnych)-np.dot(macierzwartosciwlasnych, np.ones((macierzwartosciwlasnych.shape[0], 1))).T).all() > 0.0001:
        macierzwartosciwlasnych = macierz_k(macierzwartosciwlasnych)
    return macierzwartosciwlasnych


macierz_testowa = np.array([[1., 3., 5., 7., 9.],
                            [3., 3., 3., 5., 7.],
                            [5., 3., 5., 7., 9.],
                            [7., 5., 7., 7., 9.],
                            [9., 7., 9., 9., 9.]
                            ])
print(macierz_testowa)
print(wartosciwlasne(macierz_testowa))
print(np.diag(wartosciwlasne(macierz_testowa)))
print(np.linalg.eigvals(macierz_testowa))
