# pobierz z konsoli swoje imie i wyswietl je z napisem czesc i swoje imei

from itertools import count
import struct


x = input('podaj swoje imie: ')

print('czesc, %s' %x)

# zrob se 3 zmienne na string calkowita i zmiennaprzecinkowa i potem wypisz o nich nazwe typ i wartosc
zmiennastring = 'string'
liczbaprzecinkowa = 3.0
liczbacalkowita = 2137

print('zmiennastring, typ {}, wartosc {}'.format(type(zmiennastring), zmiennastring))
print('liczbaprzecinkowa, typ {}, wartosc {}'.format(type(liczbaprzecinkowa), liczbaprzecinkowa))
print('liczbacalkowita, typ {}, wartosc {}'.format(type(liczbacalkowita), liczbacalkowita))

# zrob liste i ja wypisz polaczona # 
lista = ['piotrek', 'giga', 'mondry', 'gosc', 'kierownik']
zmienna = "#".join(lista)

print(zmienna)

a = zmienna.split('#')
print(a)

stryng = 'Metody Inżynierii Wiedzy są najlepsze'
print('{} {}'.format(stryng, len(stryng)))
print('{} , {} , {}'.format(stryng, stryng.lower(), stryng))
naprawiony = stryng
polskieznaki = 'ąćółżźńę'
angielskie = 'acolzzne'
for i in range(0,len(polskieznaki),1):
    naprawiony=naprawiony.replace(polskieznaki[i], angielskie[i])

naprawiony=naprawiony.replace(' ', '')
print('{} {}'.format(naprawiony, len(naprawiony)))
seth = set(naprawiony)
print('{} {}'.format(seth, len(seth)))
imie = 'olek'
masa = 10000
para = (imie, masa)
print('{} {}'.format(para, type(para)))

jezykiprogramowaniacoznam = ['python', 'php', 'js', 'c', 'c++', 'c#', 'lua']
print('{} {}'.format(jezykiprogramowaniacoznam, len(jezykiprogramowaniacoznam)))
print(jezykiprogramowaniacoznam.index('python'))

print( '{}\n{}'.format(lista, jezykiprogramowaniacoznam))
nowalista = lista + jezykiprogramowaniacoznam
print(nowalista)
nl2 = lista
nl2.extend(jezykiprogramowaniacoznam)
print(nl2)

slownik = {
'ukraina':'kijow', 'rosja':'moskwa','litwa':'wilno','niemcy':'berlin','czechy':'praga','slowacja':'bratyslawa',
}

print(slownik.values())
srt = sorted(slownik)
print(srt)
takiinny  = sorted(slownik, key=slownik.get)
print(takiinny)


print(bool())
print(bool(''))
print(bool(1))
print(bool(0))
print(bool(['','']))

zdanie = 'Piotrek jest najlepszym programistą HTML'

if(len(set(zdanie))>15):
    print('jest wiecej jak 15 unikalnych znakow')
else:
    print('nie ma')

if 'j' in zdanie:
    print('tak')

for i in range(0,10,1):
    print(i)

print(zmienna)

stng =''
for i in zmienna:
    if i != '#':
        stng += i
    else :
        print(stng)
        stng = ''
print(stng)