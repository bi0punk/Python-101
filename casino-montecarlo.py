from tqdm import tqdm
import time





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
        print("\n Ingrese un numero ente 0 y 36 \n")
        num_rul_jug=int(input())
        if num_rul_jug > 36:
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
        

        print("Veces a lanzar")
        veces_a_lanzar = int(input())

        contador = 1
        lista = []
        lista_choice = []

        while contador != veces_a_lanzar:
                nr = (randrange(0, 36)) # Numero al azar que entrega la ruleta
                cr = (choice(["Rojo", "Negro"])) # Color al azar que entrega la ruleta
                lista.append(nr)
                lista_choice.append(cr)
                contador = contador+1
        
        

        list_a_cadena = [str(int) for int in lista]
        
        list_choice_cadena = [str(int) for int in lista_choice]

        coma_cadena = ",".join(list_a_cadena)
        coma_cadena_choice = ",".join(coma_cadena)

        numeros = open('numeros.txt', 'w')
        numeros.write(coma_cadena)

        color_c = open('color.txt', 'w')
        color_c.write(coma_cadena_choice)


        print(lista)
                
      

       
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