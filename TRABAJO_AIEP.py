
import os 
print("*********** Sistema control de notas ***********")
print("Ingrese opcion")
print("1.- Ingresar Alumnos")
print("2.- Calcular Promedio")

opc=int(input())
os.system("clear")
if opc==1:
	nalum=[]
	nombra=(raw_input("Ingresar Nombres de alumnos: (stop para finalizar):"))
	while nombra!="stop":
		nalum.append(nombra)
		nombra=(raw_input("Ingresar Nombres de alumnos: "))
	print("\nUsted Ingreso:")
	print(len(nalum))
	print("alumnos")
 

print("Presione 1 para ingresar carreras")
opcc=int(input())
os.system("clear")
if opcc==1:
	ncarrer=[]
	nombrc=(raw_input("Ingresar nombre de la carerra: (stop para finalizar):"))
	while nombrc!="stop":
		ncarrer.append(nombrc)
		nombrc=(raw_input("Ingresar nombre de la carrera: (stop para finalizar):"))
	print("Tamano de la lista:")
	print(len(ncarrer))
	print(ncarrer)




'''notas=[]
print("Ingrese cuatas notas desea calcular")
nnot=int(input())
for x in range(nnot):
    valor=int(input("Ingrese un valor entero: "))
    notas.append(valor)

#imprimimos la lista    
print(notas)'''
