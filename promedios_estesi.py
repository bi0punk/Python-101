# promedio ---->suma/cantidad
#suma----> acumulador--->acu
#cont ----> ----> cant

cant = 0
acu = 0

while(True):
	nota= float(input("Nota: "))
	
	if(nota == -1):
		break
		
	cant = cant + 1
	acu = acu + nota
	
promedio = acu / cant
print("Promedio: "+str(promedio))
