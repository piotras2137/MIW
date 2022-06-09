import math as m
import numpy as np


def wartosciwlasne(macierz):
    return np.round(np.linalg.eigvals(macierz), decimals=5)


def svd(a):
    aat = np.dot(a, a.T)
    ata = np.dot(a.T, a)

    wartosciaat = wartosciwlasne(aat)
    wartosciata = np.sort(np.linalg.eig(ata)[0])[::-1]

    s = np.zeros((2, 3))
    tmp = [m.sqrt(i) for i in wartosciaat]
    s_temp = np.diag(tmp)
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
        u.append(np.dot(a, v.T[i]) * (1 / m.sqrt(wartosciaat[i])))
    u = np.array(u)

    return wartosciaat, wartosciata, u, s, v


np.set_printoptions(formatter={'float_kind': "{:.7f}".format})


macierz_testowa = np.array([[1, -2, 0], [2, 0, 2]])
wartosciaat, wartosciata, u, s, v = svd(macierz_testowa)

print("WARTOŚCI WŁASNE U")
print(wartosciaat)
print("WARTOŚCI WŁASNE V")
print(wartosciata)
print("MACIERZ U")
print(u)
print("WARTOŚCI SINGULARNE")
print(s)
print("MACIERZ V TRANSPONOWANE")
print(v.T)
