import numpy as np 

# definimos una función que verifica si una matriz es cuadrada
def es_cuadrada(matriz):
    return len(matriz[0]) == len(matriz)

# definimos una función que verifica si una matriz es simétrica o antisimétrica
def simetria(matriz):
    for x in range(len(matriz)):
        for y in range(x, len(matriz)):
            if matriz[x][y] != matriz[y][x]:
                return "La matriz no es simétrica"
            elif matriz[x][y] == -(matriz[y][x]):
                return "La matriz es antisimétrica"
    return "La matriz es simétrica"

# creamos las matrices a, b, y c
a = np.array([[1,2,3,4,5],[1,-1,1,-1,1],[3,3,3,3,3],[5,4,3,2,1],[6,7,8,9,10]])
b = np.array([[1,2,3,4,5],[2,1,2,1,2],[3,2,3,2,3],[4,1,2,1,4],[5,2,3,4,2]])
c = np.array([[0,2,3,4,5],[-2,0,2,1,2],[-3,-2,0,2,3],[-4,-1,-2,0,4],[-5,-2,-3,-4,0]])

# evaluamos las matrices
if es_cuadrada(a):
    print("La matriz a:", simetria(a))
else:
    print("La matriz a no es cuadrada, por lo que no es simétrica")

if es_cuadrada(b):
    print("La matriz b:", simetria(b))
else:
    print("La matriz b no es cuadrada, por lo que no es simétrica")

if es_cuadrada(c):
    print("La matriz c:", simetria(c))
else:
    print("La matriz c no es cuadrada, por lo que no es simétrica")

# creamos una matriz a partir de los últimos 3 dígitos del rut
rut = "12345678-9"
ultimos_3_digitos = rut[-3:]
matriz_rut = np.array([[int(d)*2 for d in ultimos_3_digitos], [int(d)*3 for d in ultimos_3_digitos], [int(d)*4 for d in ultimos_3_digitos]])
print("La matriz creada a partir de los últimos 3 dígitos del rut", rut, "es:")
print(matriz_rut)

