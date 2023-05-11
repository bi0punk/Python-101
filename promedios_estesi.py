class Promedio:
    def __init__(self):
        self.cant = 0
        self.acu = 0
    
    def calcular_promedio(self):
        while True:
            nota = float(input("Nota: "))
            if nota == -1:
                break
            self.cant += 1
            self.acu += nota
        promedio = self.acu / self.cant
        print("Promedio: {:.2f}".format(promedio))

promedio = Promedio()
promedio.calcular_promedio()
