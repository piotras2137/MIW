bs = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, -1, -1, -1],
    [1, 1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, -1, -1],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, -1],
]


"""
1) sprawdzic czy B ma wektory ortogonalne
    B razy B.T  czy da nam macierz diagonalna

2) znormalizować wektory w B 

3) tak zmodyfikowaną B sprawdzić czy jest ortonormalna
    czyli jak B razy B.T da nam macierz jednostkowa

4) przeprowadzić wektor [ 8 6 2 3 4 6 6 5] z bazy standardowej do bazy B po normalizacji

program i ręcznie
"""
