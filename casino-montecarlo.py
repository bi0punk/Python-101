from tqdm import tqdm
import random


def obtener_color():
    print("Ingrese colores para apostar")
    print("1) Rojo")
    print("2) Negro")
    while True:
        try:
            col_apuesta = int(input())
            if col_apuesta == 1:
                return 'Rojo'
            elif col_apuesta == 2:
                return 'Negro'
            else:
                print("Ingrese una opción válida")
        except ValueError:
            print("Ingrese una opción válida")


def obtener_numero():
    while True:
        try:
            num_rul_jug = int(input("Ingrese un número entre 0 y 36: "))
            if num_rul_jug >= 0 and num_rul_jug <= 36:
                return num_rul_jug
            else:
                print("Ingrese un número dentro del rango")
        except ValueError:
            print("Ingrese un número válido")


def lanzar_ruleta(veces_a_lanzar):
    lista = []
    lista_choice = []

    for _ in tqdm(range(veces_a_lanzar)):
        nr = random.randint(0, 36)  # Número al azar que entrega la ruleta
        cr = random.choice(["Rojo", "Negro"])  # Color al azar que entrega la ruleta
        lista.append(nr)
        lista_choice.append(cr)

    return lista, lista_choice


def resumen_apuesta(mon_apuesta, color, num_rul_jug):
    print("Resumen Apuesta")
    print("Monto:", mon_apuesta)
    print("Color:", color)
    print("Número:", num_rul_jug)


def resultado_ruleta(nr, cr):
    print("Resultado Ruleta")
    print("Color:", cr)
    print("Número:", nr)


def calcular_ganancia(mon_apuesta, nr, color, cr):
    if nr != num_rul_jug and color == cr:  # Ganando el 20% del dinero apostado
        ganancia = mon_apuesta * 0.2
        print("Usted ha ganado:", ganancia)

    elif nr == num_rul_jug and color != cr:  # Ganando el 100% del dinero apostado
        ganancia = mon_apuesta * 2
        print("Usted ha ganado:", ganancia)

    elif nr == num_rul_jug and color == cr:  # Ganando el 200% del dinero apostado
        ganancia = mon_apuesta * 4
        print("Usted ha ganado:", ganancia)

    else:
        print("Mala suerte, no ganó nada")


if __name__ == "__main__":
    print("#####################")
    print("# RULETA MONTECARLO #")
    print("#####################")

    mon_apuesta = int(input("Ingrese el monto a apostar: "))
    color = obtener_color()
    num_rul_jug = obtener_numero()

    resumen_apuesta(mon_apuesta, color, num_rul_jug)

    op_rul = input("Presione Enter para lanzar Ruleta: ")

    if op_rul == "":
        veces_a_lanzar = int(input("Veces a lanzar")
