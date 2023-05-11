import random

lista = [0] * 6
print("Colocando bala en una posición...")

pos = random.randint(0, 5)
lista[pos] = 1

while True:
    a = int(input("Para disparar, seleccione una posición: "))
    if lista[a] == 1:
        print("¡BANG! Has perdido.")
        break
    else:
        print("Sigues vivo.")
print("Fin del juego.")
