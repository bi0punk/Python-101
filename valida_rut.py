import sys
import re

def validarRut(rut):
    rut = re.sub("[^0-9kK]", "", rut)
    aux = rut[:-1]
    dv = rut[-1]
    factors = [2, 3, 4, 5, 6, 7]
    factors.reverse()
    digits = [int(d) for d in reversed(aux)]
    s = sum(d * f for d, f in zip(digits, factors))
    res = (11 - (s % 11)) % 11
    valid_dv = str(res) if res < 10 else "K"
    return valid_dv == dv

def main():
    print(validarRut(sys.argv[1]))

if __name__=="__main__":
    main()
