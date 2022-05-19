from matplotlib import lines


def haslo(passwd):
    dlugosc = False
    maduze = False
    mamale = False
    mawykrzyknik = False
    maliczby = False

    for i in passwd:
        for j in range(0,10,1):
            if i == str(j):
                maliczby = True

        if ord(i)<91 and ord(i)>64:
            maduze = True
        
        if ord(i)<123 and ord(i)>96:
            mamale = True

        if i == '!':
            mawykrzyknik=True 

    return maduze and mamale and mawykrzyknik and len(passwd)>10


print(haslo('Piotras2137!'))
print(haslo('haslo123'))


lista = [2,1,3,7,99]
for i in lista:
    if i==99:
        continue
    print(i)


def czynalezy(co, gdzie):
    nalezy = False
    while(co in gdzie):
        nalezy = True
        break
    return nalezy


print(czynalezy('piotrek', 'piotreknajlepszy'))
print(czynalezy(8, [1,2,3,4,6,7]))


x = open('dupa.txt', 'w')
x.write('metody\n')
x.write('inzynierii\n')
x.write('wiedzy')
x.close()
y = open('dupa.txt', 'r')
z = y.readlines()
y.close()
for i in z:
    print(i)

for i in z:
    print(i, end='')


listajezykow = ['html', 'css', 'js', 'python', 'c', 'c++', 'lua']

with open('jezyki.txt', 'w') as x:
    for i in listajezykow: 
        print(i, file=x) 

with open('jezyki.txt', 'r') as y:
    z = y.readlines()

for i in z:
    print(i, end='')


listamiast = ['Olsztyn', 'Warszawa', 'Krakow', 'Lodz']
lambada = lambda x : x[0:3] 
kek = map(lambada, listamiast)
print(kek)
kekw = list(kek)
print(kekw)

powiedzmyzetolista = ['plik.txt', 'plik.doc', 'plik.py', 'plik.xd', 'chuj.php', 'niedziala.txt', 'pasy.txt']

def zwrotzrozszerzeniem(lista, rozszerzenie):
    nowalista = []
    for i in lista:
        x = i.split('.')
        if x[len(x)-1] == rozszerzenie:
            nowalista.append(i)

    return nowalista

def rozszerzenie(lista, rozszerzenie):
    nl = []
    for i in lista:
        if rozszerzenie in i:
            nl.append(i)

    return nl 


A = zwrotzrozszerzeniem(powiedzmyzetolista, 'txt')
print(A)
print(rozszerzenie(powiedzmyzetolista,'.txt'))