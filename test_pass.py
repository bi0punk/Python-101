import random


minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"


combinacion = minusculas + mayus + numeros

largo = 9 #valormaximo

contraseña = "".join(random.sample(combinacion, largo))
print(contraseña)