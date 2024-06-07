def analizar_numero(numero):
    par = lambda x: 'Par' if x % 2 == 0 else 'Impar'
    positivo = lambda x: 'Positivo' if x > 0 else 'Negativo' if x < 0 else 'Cero'
    divisible_por_3 = lambda x: 'Sí' if x % 3 == 0 else 'No'
    divisible_por_5 = lambda x: 'Sí' if x % 5 == 0 else 'No'
    divisible_por_3_y_5 = lambda x: 'Sí' if x % 3 == 0 and x % 5 == 0 else 'No'
    resultado = {
        'Par o Impar': par(numero),
        'Positivo, Negativo o Cero': positivo(numero),
        'Divisible por 3': divisible_por_3(numero),
        'Divisible por 5': divisible_por_5(numero),
        'Divisible por 3 y 5': divisible_por_3_y_5(numero)
    }
    return resultado
numero = int(input("Ingrese un número entero: "))
resultado = analizar_numero(numero)
print(resultado)