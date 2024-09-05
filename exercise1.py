import math

def calcular_perimetro(altura):
    lado = (2 * altura) / math.sqrt(3)
    perimetro = 3 * lado
    return perimetro

# Entrada de la altura
altura = float(input("Introduce la altura del triángulo equilátero: "))

# Calcular y mostrar el perímetro
perimetro = calcular_perimetro(altura)
print(f"El perímetro del triángulo equilátero es: {perimetro:.2f}")