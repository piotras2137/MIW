import math as meth 

with open('australian.dat', 'r') as x:
    wyniki =[]
    for line in x.readlines():
        floateddata = [float(j) for j in line.strip('\n').split(' ')]
        wyniki.append(floateddata)


with open('australian.dat', 'r') as x:
    kek = [ [float(j) for j in line.strip('\n').split(' ')]  for line in x.readlines()]


chybawjednejlinii = [ [float(j) for j in line.strip('\n').split(' ')]  for line in open('australian.dat', 'r').readlines()]


def euklides(e1, e2):
    wynik = 0 
    for i in range(0,len(e1)-1, 1):
        wynik+=meth.pow(e1[i]-e2[i],2) 
    return meth.sqrt(wynik)



print(euklides(chybawjednejlinii[0], chybawjednejlinii[1]))
print(euklides(chybawjednejlinii[0], chybawjednejlinii[2]))
print(euklides(chybawjednejlinii[0], chybawjednejlinii[3]))