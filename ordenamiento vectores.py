# Este codigo ha sido generado por el modulo psexport 20160408-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from random import randint

if __name__ == '__main__':
	arreglo = int()
	i = int()
	numin = int()
	minimo = int()
	j = int()
	aux = int()
	print("Ingrese la cantidad de datos que va a ingresar")
	numin = int(input())
	arreglo = [int() for ind0 in range(numin)]
	print("Este es el vector original:")
	print("")
	for i in range(numin):
		arreglo[i-1] = randint(0,9)
		print(arreglo[i-1])
	for i in range(numin):
		minimo = i
		for j in range(i,numin):
			# con < ordena ascendente, con > ordena descendente
			if arreglo[j-1]<arreglo[minimo-1]:
				minimo = j
		aux = arreglo[i-1]
		arreglo[i-1] = arreglo[minimo-1]
		arreglo[minimo-1] = aux
	print("Este es el vector ordenado:")
	for i in range(numin):          
		print (arreglo[i-1])
