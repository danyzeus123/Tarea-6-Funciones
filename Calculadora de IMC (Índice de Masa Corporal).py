peso = float(input("Ingrese su peso en kg: "))
altura_cm = float(input("Ingrese su altura en cm: "))

def calculo_del_imc(peso, altura_cm):
    altura_metro = altura_cm / 100 
    imc = peso / (altura_metro ** 2)  
    return imc
def clasificacion_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
imc = calculo_del_imc(peso, altura_cm)
categoria = clasificacion_imc(imc)
print(f"Su IMC es: {imc:.2f}")
print(f"Clasificación: {categoria}")