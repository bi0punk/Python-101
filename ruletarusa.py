import random

num_positions = 6
positions = [0] * num_positions

print("Verificando posiciones...")
bullet_position = random.randint(0, num_positions - 1)
positions[bullet_position] = 1

while True:
    shoot_position = int(input("Para disparar, seleccione una posición: "))
    
    if positions[shoot_position] == 1:
        print("¡Bala encontrada! Usted está muerto.")
        break
    else:
        print("Sigue vivo.")
        
print("Juego terminado.")
