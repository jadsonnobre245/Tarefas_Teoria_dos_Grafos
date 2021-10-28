import numpy as npy
from numpy.linalg import inv


a = [
    [5,2],
    [3,4]]


diag = []
for i in range (len(a)):
    diag.append([0]*len(a[0]))

for i in range (len(a)):
    diag[i][i] = a[i][i]


diag = npy.matrix(diag)



a = npy.matrix(a)
d = inv(diag)
n = a - diag
b = npy.matrix([[2],[1]])
x = npy.matrix([[npy.random.randint(1,100)],[npy.random.randint(1,100)]])

#encontra pontos fixos
for i in range(1000):
    x = d * (b - (n*x))

print(inv(diag))
print(a - diag)
print(b)
print(x)