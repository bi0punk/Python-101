print("Hola mundo calculadora")
print("Cálculo de promedio")
print("1.- Ingresar notas")
print("2.- Calcular promedio")

opcion = int(input())

if opcion == 1:
    pnum = int(input("Ingrese nota 1: "))
    snum = int(input("Ingrese nota 2: "))
    resultado = pnum + snum
    print(f"El resultado es: {resultado}")
    
elif opcion == 2:
    rnum = int(input("Ingrese el primer numero: "))
    r2num = int(input("Ingrese el segundo numero: "))
    resultador = rnum - r2num
    print(f"El resultado es: {resultador}")
    
else:
    print("Opción no válida")
