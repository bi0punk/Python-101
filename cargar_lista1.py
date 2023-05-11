nalum = []
while True:
    nombal = input("Ingrese Nombre de Alumno: ")
    if nombal.lower() == "stop":
        break
    nalum.append(nombal)
print(f"Cantidad de alumnos registrados: {len(nalum)}")
