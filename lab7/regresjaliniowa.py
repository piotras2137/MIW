import math as m
import numpy as np


def regresjaliniowa(macierz):
    # zrobienie macierzy zawierajacej 1 i x dla kazdego x macierzy
    x = [[1, i[0]] for i in macierz]
    x = np.array(x)
    # zrobienie macierzy Y z macierzy
    y = [i[1] for i in macierz]
    y = np.array(y)
    return np.dot(np.dot(np.linalg.inv(np.dot(x.T, x)), x.T), y)


# przykladowa macierz
macierz = np.array(
    [
        [2, 1],
        [3, 7],
        [6, 9],
    ]
)

print(regresjaliniowa(macierz))
