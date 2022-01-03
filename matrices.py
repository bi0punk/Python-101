#importamos la libreria numpy

import numpy as np 

#Pregunta 1

#Crear tres matrices y evaluar si estan correctas o no.


    #creamos una funcion llamada 'es_cuadrada' y le pasamos el parametro matriz
    #ciclo if que evalua condicion si largo de matriz es igual al largo de la matriz
    #en caso verdadero retornara un 1 
    #caso contrario un 0


def es_cuadrada(matriz):
    if len(matriz[0])==len(matriz):
        return 1
    else:
        return 0


    #creamos funcion 'simetria' y le pasamos el parametro matriz
    # creamos una variable 'sim' y le asignamos el valor de True
    # creamos un ciclo y recorremos en el rango de la longitud de la matriz
    #dentro del ciclo anterior, creamos otro for, para recorrer valor de i , iniciando desde x y la largo de la 'matriz'
    #bucle if que evalua si la matrix x  y   es distinta a matriz y  x 
    #si es correcto variable 'sim' toma el valor de False
    #y x es igual al largo de la matriz
    #cerramos bucle con break

    #ciclo elif que evalua si matriz x y   es igual a matriz y x negativa
    #si se cumple condicion 'sim' sera igual a 0
    #x sera igual a largo de la matriz
    #cerramos con break


def simetria(matriz):
    sim=True
    for x in range(0,len(matriz)):
        for y in range(x,len(matriz)):
            if (matriz[x][y] != matriz[y][x]):
                sim=False
                x=len(matriz)
                break
            elif (matriz[x][y] == -(matriz[y][x])):
                sim=0
                x=len(matriz)
                break

    #Ciclo if si la variable 'sim' tiene el valor de True
    #imprime "La matriz"
    #imprime matriz + es simetrica
    #ciclo elif evalua si 'sim' es igual a 0:
    #en caso de que se cumpla la condicion imprime que la matriz es antisimetrica


    if sim==True:
        print("La matriz\n")
        print(matriz," \n es simetrica\n")
    elif sim==0:
        print("La matriz\n",matriz,"\n es antisimetrica \n")
    else:
        print( "\n La matriz",matriz,"\n no es simetrica \n") 


#creamos las variables a, b, c y le damos la funcion np.array, para crear una matriz y asi poder operar con ella de manera eficiente
# creamos una variable re, que llama a la funcion es_cuadrada y le pasamos las variables que corresponde a c/u de las mastricea


a=np.array([[1,2,3,4,5],[1,-1,1,-1,1],[3,3,3,3,3],[5,4,3,2,1],[6,7,8,9,10]])
b=np.array([[1,2,3,4,5],[2,1,2,1,2],[3,2,3,2,3],[4,1,2,1,4],[5,2,3,4,2]])
c=np.array([[0,2,3,4,5],[-2,0,2,1,2],[-3,-2,0,2,3],[-4,-1,-2,0,4],[-5,-2,-3,-4,0]])
re_a=es_cuadrada(a)
re_b=es_cuadrada(b)
re_c=es_cuadrada(c)




#ciclo que evalua si re_a es igual a 1:
#si se cumple condicion x sera igual a simetria(funcion) con el parametro de a
#caso contrario
#imprime que no es cuadrada, no es siemtrica

#vovlemos a evaluar pero esta vez re_b si es igual a 1
#si se cumple condicion x sera igual a simetria(funcion) con el parametro de b
#caso contrario
#imprime que no es cuadrada, no es siemtrica

#ciclo if se evalua pero la variable de re_c si es igual a 1:
#si se cumple condicion x sera igual a simetria(funcion) con el parametro de c
#else, caso contrario
##imprime que no es cuadrada, no es siemtrica




if re_a==1:
    x=simetria(a)
else:
    print("La matriz no es cuadrada, por lo que no es simetrica")
if re_b==1:
    x=simetria(b)
else:
    print("La matriz no es cuadrada, por lo que no es simetrica")
if re_c==1:
    x=simetria(c)
else:
    print("La matriz no es cuadrada, por lo que no es simetrica")









#Pregunta 2

#Crear una matriz a partir de los ultimos 3 numeros del rut.












#importamos modulo numpy, (mo es necesario)

import numpy as np


#creamos una variable i con el valor de 1

i=1



#creamos otra variable n, pero esta vez es un input, que ademas lleva la impresión "Los tres ultimos digitos de su rut sin digito verificador"

n=int(input("Los tres ultimos digitos de su rut sin digito verificador: "))


#creamos una lista vacia llamada lista
#ciclo while que evalua mientras el largo de la lista sea menor que n(variable)
#dentro del while, creamos dos variables, una tipo lista llamada h y otra llamada j asignando el valor de 1
#y volvemos a crear otro ciclo while que dice que mientras j sea menor o igual a n
#variable 'po' sera igual 2 potencia n-1
#variable 'ka' sera igual 3 potencia j
#h.append metodo para agregar a la lista el valor de (po*ka)
#continuando a j se suma 1
#salimos del ciclo e implementamos lista.append(h) para agregar h a la lista llamada 'lista'
#de igual manera le sumamos 1 al contador i


lista=[]
while len(lista)<n:
    h=[]
    j=1
    while j <=n:
        po=2**(n-i)
        ka=3*+j
        h.append(po*ka)
        j+=1
    lista.append(h)
    i+=1


#creamos variable l tipo array de numpy pasando como parametro 'lista'
#variable ma seria igual a metodo matrix pasando parametro 'l'
#variable ta seria igual a 'ma' * 'ma' , multiplicacion
#variable A seria igual a 'ma' + 'ta'


l=np.array(lista)
ma=np.matrix(l)
ta=ma*ma
A=ma+ta

#creamos una impresion para las variables 'ta', 'ma', 'A', , con las funciones diagonal, max y min respectivamente

print(ta.diagonal())
print(ma.max())
print(A.min())
