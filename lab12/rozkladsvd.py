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


np.set_printoptions(formatter={'float_kind': "{:.7f}".format})
a = np.array([[1., 2., 0.], [2., 0., 2.]])
aat = np.dot(a, a.T)
ata = np.dot(a.T, a)

wartosci_wlasne_aat = wartosciwlasne(aat)
wartosci_wlasne_ata = np.sort(np.linalg.eig(ata)[0])[::-1]

s = np.zeros((2, 3))
s_temp = np.diag([m.sqrt(i) for i in wartosci_wlasne_aat])
for i in range(len(s_temp[0])):
    for j in range(len(s_temp[1])):
        s[i][j] = s_temp[i][j]

v = []
for i in range(len(ata[0])):
    wektor_v = []
    for j in range(len(ata[0]), 0, -1):
        wektor_v.append(np.linalg.eigh(ata)[1][i][j-1])
    v.append(wektor_v)
v = np.array(v)

u = []
for i in range(len(aat[0])):
    u.append(np.dot(a, v.T[i]) * (1 / m.sqrt(wartosci_wlasne_aat[i])))
u = np.array(u)

print("ROZKŁAD SVD")
print("\n")
print("WARTOŚCI WŁASNE U")
print(wartosci_wlasne_aat)
print("WARTOŚCI WŁASNE V")
print(wartosci_wlasne_ata)
print("MACIERZ U")
print(u)
print("WARTOŚCI SINGULARNE")
print(s)
print("MACIERZ V TRANSPONOWANE")
print(v.T)
print("SPRAWDZENIE")
print(np.dot(np.dot(u, s), v.T))
