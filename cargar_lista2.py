


nalum=[]
nombra=(raw_input("Ingresar Nombres de alumnos: (stop para finalizar):"))
while nombra!="stop":
    nalum.append(nombra)
    nombra=(raw_input("Ingresar valor (stop para finalizar):"))
    break
print("Tamano de la lista:")
print(len(nalum))
print(nalum)
