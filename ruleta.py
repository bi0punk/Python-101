
import random

lista=[]
print("verificando")
for pos in range(0, 6):
		lista.append(0)
		
print("Colocado bala en posicion")

pos=random.randrange(0, 5)
lista[pos]=1
bandera=True
while bandera:
	a=int(input("Para dispara seleccione una posicion:  "))
	if lista[a]==1:
		bandera=False
	else:
		print("sigues vivo")
print("usted esta... uc")