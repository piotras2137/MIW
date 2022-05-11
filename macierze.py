def wyznacznik(macierz):
    x = len(macierz)
    if x == 2:
        return macierz[0][0]*macierz[1][1]-macierz[0][1]*macierz[1][0]
    
    dodawanie = []
    odejmowanie = []
    for i in range(0, x, 1):
        Z = 1
        for j in range(0,x,1):
            print(i,' ',j,' ', macierz[(i+j)%(x)][j%(x)])
            Z*=macierz[(i+j)%(x)][j%(x)]
        
        dodawanie.append(Z)

    for i in range(x-1, -1, -1):
        Z = 1
        for j in range(0, x, 1):
            if i-j<0:
                Z*= macierz[(i-j)+x][j%(x)]
            else:
                Z*= macierz[i-j][j%(x)]
        odejmowanie.append(Z)

    print(dodawanie)
    print(odejmowanie)

    wynik = 0
    for i in dodawanie:
        wynik+=i
    for i in odejmowanie:
        wynik-=i
    return wynik

macierz = [[2,1],[3,7]]

print(wyznacznik(macierz))

