
print("hola mundo calculadora")
  
print("Calculo de promedio")
print(" 1.- Ingresar notas ")
print(" 2.- calcular promedio")

opcion=int(input())
if opcion==1:

	print("Ingrese nota 1 ")
	pnum=int(input())
	print("Ingrese el segundo numero")
	snum=int(input())
	resultado=pnum+snum
	print("el resultado es ") +str(resultado)

if opcion==2:
	print("ha seleccionado la resta")
	print("ingrese el primer numero")
	rnum=int(input())
	print("Ingrese el segundo numero")
	r2num=int(input())
	resultador=rnum-r2num
	print("el resultado es ") +str(resultador)
	
