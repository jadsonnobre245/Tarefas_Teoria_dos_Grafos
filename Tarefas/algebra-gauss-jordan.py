matriz = [ 
    [1,1,1,1,0,0],
    [2,1,1,0,1,0],
    [1,1,2,0,0,1]]
print('Matriz aumentada')
for i in matriz:
 print(i)

for i in range(len(matriz)-1):
 for j in range (i+1,len(matriz)):
   op = (matriz[j][i]/matriz[i][i])
   for k in range(len(matriz[0])):
    matriz[j][k] = matriz[j][k] - op * matriz[i][k]
  
for i in range(len(matriz)-1,0,-1):
  for j in range (i-1,-1,-1):
    op = (matriz[j][i]/matriz[i][i])
    for k in range(len(matriz[0])):
     matriz[j][k] = matriz[j][k] - op * matriz[i][k]

for i in range(len(matriz)):
  pivo = matriz[i][i]
  for j in range(len(matriz[0])):
    matriz[i][j] = matriz[i][j] / pivo
  

print('Matriz gauss jordan')
for i in matriz:
 print(i)

