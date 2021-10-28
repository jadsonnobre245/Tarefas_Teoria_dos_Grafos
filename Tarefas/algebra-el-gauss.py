matriz = [ 
    [1,1,0,3,4],
    [2,1,-1,1,1],
    [3,-1,-1,2,-3],
    [-1,2,3,-1,4]]
print('Matriz aumentada')
for i in matriz:
 print(i)

for i in range(len(matriz)-1):
 for j in range (i+1,len(matriz)):
   op = (matriz[j][i]/matriz[i][i])
   for k in range(len(matriz[0])):
    matriz[j][k] = matriz[j][k] - op * matriz[i][k] 
print('Matriz escalonada')
for i in matriz:
 print(i)

var = []
for i in range(len(matriz)):
  var.append(0)

for i in range(len(matriz)-1,-1,-1):
  soma = 0
  for j in range(len(matriz[0])-1):
    soma += matriz[i][j]*var[j]
  var[i] = -soma +matriz[i][len(matriz[0])-1]
  var[i] = var[i] / matriz[i][i]

print('valor das variaveis',var)

