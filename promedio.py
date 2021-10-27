
print("Sisitema de calculo de promedios")
print("Seleccione que opcion a realizar")
print(" 1.- Ingresar datos  alumnos")
print(" 2.- Mostrar promedios")  
opc=(int(input(hola))


"""def main():

	notas = []
	while True:
		print "Ingrese Nota: \n"
		num = input()
		if num >= 71:
			print("\nRango Excedido, Ingrese la nota correcta")
			
		if num == "salir":
			
			break
		elif num >= 0:
			notas.append(num)
			print "\n Promedio actual: ",sum(notas)/float(len(notas)), "\n"			
		else:
			try:
				print "Promedio actual: ",sum(notas)/float(len(notas)),"\n"
			except:
				print "Primero ingrese un valor positivo"
main()
