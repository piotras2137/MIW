import numpy as np


def gausrownania(iloscniewiadomych, macierz):
    wynik = np.zeros(iloscniewiadomych)
    for i in range(iloscniewiadomych):
        if macierz[i][i] == 0.0:
            print("dzielenie przez zero")
            return 0
        else:
            for j in range(iloscniewiadomych):
                if i != j:
                    wsp = macierz[j][i] / macierz[i][i]
                    for k in range(iloscniewiadomych + 1):
                        macierz[j][k] = macierz[j][k] - wsp * macierz[i][k]

    for k in range(iloscniewiadomych):
        wynik[k] = macierz[k][iloscniewiadomych] / macierz[k][k]
    return wynik


def gausmacierz(stopien, macierz):
    macierz2 = np.zeros((stopien, 2 * stopien))
    wynik = np.zeros((stopien, stopien))
    for i in range(stopien):
        for j in range(stopien):
            macierz2[i][j] = macierz[i][j]
    for i in range(stopien):
        for j in range(stopien):
            if i == j:
                macierz2[i][j + stopien] = 1
    for i in range(stopien):
        if not macierz2[i][i] == 0.0:
            for j in range(stopien):
                if i != j:
                    wsp = macierz2[j][i] / macierz2[i][i]
                    for k in range(stopien * 2):
                        macierz2[j][k] = macierz2[j][k] - wsp * macierz2[i][k]
        else:
            print("Nie można dzielić przez 0")
            return 0
    for i in range(stopien):
        dzielnik = macierz2[i][i]
        for j in range(2 * stopien):
            macierz2[i][j] = macierz2[i][j] / dzielnik
    for i in range(stopien):
        for j in range(stopien):
            wynik[i][j] = macierz2[i][j + stopien]
    return wynik


macierz_testowa = np.array([[2, 1, 3, 7], [4, 2, 0, 7], [7, 7, 7, 1]])
macierz_testowa2 = np.array(
    [[2., 1., 3., 7.], [6., 6., 6., 12.], [3., 5., 2., 4.]])
macierz_testowa3 = np.array([[2., 1., 1., 1.], [5., 2., 2., 1.], [
                            2., 1., 3., 0.], [1., 1., 2., 1.]])
print(gausrownania(3, macierz_testowa))
print(gausrownania(3, macierz_testowa2))
print(gausmacierz(4, macierz_testowa3))
