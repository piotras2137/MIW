import numpy as np

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making numpy array of n x n+1 size and initializing
# to zero for storing augmented matrix
a = np.zeros((n, n+1))

# Making numpy array of n size and initializing
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input('a['+str(i)+'][' + str(j)+']='))


for i in range(n):
    if a[i][i] == 0.0:
        print('dzielenie przez zero')
        break

    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

for i in range(n):
    x[i] = a[i][n]/a[i][i]

for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
