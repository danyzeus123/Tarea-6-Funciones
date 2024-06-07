import math
def area_cuadrado(lado):
    return lado * lado
def perimetro_cuadrado(lado):
    return 4 * lado
def area_triangulo_equilatero(lado):
    return (math.sqrt(3) / 4) * (lado ** 2)
def perimetro_triangulo_equilatero(lado):
    return 3 * lado
def area_triangulo_rectangulo(base, altura):
    return (base * altura) / 2
def perimetro_triangulo_rectangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3
def area_triangulo_isosceles(base, altura):
    return (base * altura) / 2
def perimetro_triangulo_isosceles(lado1, lado2, base):
    return lado1 + lado2 + base
def area_circulo(radio):
    return math.pi * (radio ** 2)
def perimetro_circulo(radio):
    return 2 * math.pi * radio
def area_rectangulo(base, altura):
    return base * altura
def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)
lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
print("Área del cuadrado:", area_cuadrado(lado_cuadrado))
print("Perímetro del cuadrado:", perimetro_cuadrado(lado_cuadrado))
lado_triangulo = float(input("Ingrese el lado del triángulo equilátero: "))
print("Área del triángulo equilátero:", area_triangulo_equilatero(lado_triangulo))
print("Perímetro del triángulo equilátero:", perimetro_triangulo_equilatero(lado_triangulo))
radio_circulo = float(input("Ingrese el radio del círculo: "))
print("Área del círculo:", area_circulo(radio_circulo))
print("Perímetro del círculo:", perimetro_circulo(radio_circulo))
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
print("Área del rectángulo:", area_rectangulo(base_rectangulo, altura_rectangulo))
print("Perímetro del rectángulo:", perimetro_rectangulo(base_rectangulo, altura_rectangulo))