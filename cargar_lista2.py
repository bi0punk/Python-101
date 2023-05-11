nalum = []
while True:
    nombra = input("Ingresar Nombres de alumnos: (stop para finalizar): ")
    if nombra == "stop":
        break
    nalum.append(nombra)
print(f"Cantidad de alumnos registrados: {len(nalum)}")
print(nalum)
