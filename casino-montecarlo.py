


from random import randrange, choice


print (" #####################")
print (" # RULETA MONTECARLO #")
print (" #####################")


print("Ingrese el monto a apostar \n")

#guardamos ingreso de valor en  variable din_apuesta, tipo entero

mon_apuesta = int(input())


""" print("\n Usted a apostado: " +str(din_apuesta)) """
""" print(din_apuesta) """

#seleccion de colores rojo o negro

print("""\n Ingrese colores para apostar

          1) Rojo
          2) Negro   \n""")

#ciclo if para determinar colores

col_apuesta = int(input())
if col_apuesta == 1:
        color = 'Rojo'  #asignamos una variable tipo string para mostrar en resumen

if col_apuesta ==2:
        color = 'Negro'

bandera = True
while bandera:
        print("\n Ingrese un numero ente 0 y 20 \n")
        num_rul_jug=int(input())
        if num_rul_jug > 20:
                print("Ingrese un numero dentro del rango")
        else:
                bandera = False
 
print(" _____________________________")
print("|    Resumen Apuesta ")
print("|-----------------------------|")
print("|  Monto: " +str(mon_apuesta))
print("|  Color: " +str(color))
print("|  Numero: "+str(num_rul_jug))
print("|_____________________________|")


#logica de premios

print("\n Presione 1 Para lanzar Ruleta")
op_rul = int(input())

if op_rul == 1:
        nr = (randrange(0, 20)) # Numero al azar que entrega la ruleta
        cr = (choice(["Rojo", "Negro"])) # Color al azar que entrega la ruleta
        print(" _______________________________")
        print("|       Resultado Ruleta        |")
        print("|-------------------------------|")
        print("|     Color: " +str(cr))
        print("|     Numero: " +str(nr))
        print("|_______________________________|")


        if nr != num_rul_jug and color == cr:  # Ganando el 20% del dinero apostado
                ganancia = mon_apuesta*20/100

                print(" ____________________________")
                print("| Usted ha ganado: " +str(ganancia))
                print("|____________________________|")


        if nr == num_rul_jug and color != cr:  # Ganando el 100% del dinero apostado
                ganancia = mon_apuesta*2
                print(" ________________________")
                print("|  Usted ha ganado: " +str(ganancia))
                print("| _______________________|")

        if nr == num_rul_jug and color == cr: # ganando el 200% de dinero apostado
                ganancia = mon_apuesta*4
                print(" __________________________")
                print("|  Usted ha ganado: " +str(ganancia))
                print("|__________________________|")

        if nr != num_rul_jug and color != cr:
                gananancia = 0
                print(" _______________________________")
                print("|   Mala suerte, no gano nada   |")
                print("|_______________________________|")