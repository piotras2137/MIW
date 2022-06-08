import numpy as np

# po transponowaniu
bt = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, -1, -1],
    [1, 1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, -1, -1],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1],
]

BT = np.array(bt)

# macierz bez transpozycji
B = BT.T
print(B)
print(BT)
# przemnozenie B * BT
dot = np.dot(BT, BT.T)
print(dot)
# sprawdzenie czy macierz b ma wetkory ortogonalne
ort = True
for i in range(0, len(B)):
    for j in range(0, len(B)):
        if i != j and np.dot(B[i], B[j]) != 0:
            ort = False

if ort:
    print('macierz jest ortogonalna')
else:
    print('macierz nie jest ortogonalna')


ort = True
for i in range(0, len(dot)):
    for j in range(0, len(dot)):
        if i != j and np.dot(dot[i], dot[j]) != 0:
            ort = False

if ort:
    print('macierz jest ortogonalna')
else:
    print('macierz nie jest ortogonalna')


# sprawdzenie czyjest to macierz diagonalna
diag = True
for i in range(0, len(dot)):
    for j in range(i, len(dot[i])):
        if dot[i][j] != 0 and i != j:
            diag = False
            break
if diag:
    print('macierz jest diagonalna')
else:
    print('macierz nie jest diagonalna')


# macierz ortonormalna

norm = np.array([x / pow((np.dot(x, x)), 1/2) for x in dot], dtype=np.float64)
ortnorm = True
for i in range(0, len(norm)):
    for j in range(0, len(norm[i])):
        if abs(norm[i][j]) > 1:
            ortnorm = False
            break
print(np.dot(dot, BT))
if ortnorm:
    print("macierz jest ortonormalna")
else:
    print("nie jest ortonormalna")


wektor = np.array([8, 6, 2, 3, 4, 6, 6, 5])
nowywektor = np.dot(dot, wektor.T)
print(nowywektor)
