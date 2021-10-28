import numpy as np
from matplotlib import pyplot as plt

def vertice_star(p_0, p_1):
    x1, x2 = p_0[0], p_1[0]
    y1, y2 = p_0[1], p_1[1]

    ax.plot([x1, x2], [y1, y2], 'y-')

def criar_madala(p, ang): #Função para criar a a rotação da matriz
    c_mandala = np.array([
        [np.cos(np.deg2rad(ang)), -np.sin(np.deg2rad(ang))],
        [np.sin(np.deg2rad(ang)),  np.cos(np.deg2rad(ang))]
    ])

    rot = np.matmul(c_mandala, p) #Multiplica a matriz de rotação pelo vetor

    return rot

def print_star(_star, _cor, _angulo_rotacao):
    for i in range(len(_star)):
        vetor = criar_madala(_star[i], _angulo_rotacao)
        _star[i] = vetor

star = [
    [-0.95, 4.86],
    [0.09, 10.26],
    [1.19, 4.92],
    [-6.95, 5.84],
    [-1.71, 3.48],
    [-4.51, -2.92],
    [0, 3],
    [5.03, -2.62],
    [1.75, 3.34],
    [7.33, 5.9]  
]


_, ax = plt.subplots()

vertice_star(star[0],star[1])
vertice_star(star[1],star[2])
vertice_star(star[0],star[3])
vertice_star(star[3],star[4])
vertice_star(star[4],star[5])
vertice_star(star[5],star[6])
vertice_star(star[6],star[7])
vertice_star(star[7],star[8])
vertice_star(star[8],star[9])
vertice_star(star[9],star[2])

ax.set_title('Estrela Mandala')
ax.figure.set_size_inches(10, 10)
ax.set_xlim([-11,11])
ax.set_ylim([-11,11])


timeuot = 0.2
while True:
	print_star(star, 'co', 10)
	vertice_star(star[0],star[1])
	vertice_star(star[1],star[2])
	vertice_star(star[0],star[3])
	vertice_star(star[3],star[4])
	vertice_star(star[4],star[5])
	vertice_star(star[5],star[6])
	vertice_star(star[6],star[7])
	vertice_star(star[7],star[8])
	vertice_star(star[8],star[9])
	vertice_star(star[9],star[2])	
	plt.draw()



	plt.pause(timeuot)
