def imc(peso, altura):
    resultado = peso / altura ** 2
    return resultado

print(f"O IMC de uma pessoa com 78kg e 1,83m é {imc(78, 1.83)}")

################################################

from math import pi

def calc_area(base, altura, tipo):
    if tipo == "R":     # Retângulo
        return base * altura
    elif tipo == "T":   # Triângulo
        return base * altura / 2
    elif tipo == "E":   # Elipse
        return (base / 2) * (altura / 2) * pi
    else:
        return None
    
print(f"Área retângulo 22x47: {calc_area(22, 47, 'R')}")
print(f"Área triângulo 12,5x25: {calc_area(12.5, 25, 'T')}")
print(f"Área elipse 20x30: {calc_area(20, 30, 'E')}")
print(f"Área inválida 8x11,5: {calc_area(8, 11.5, 'W')}")