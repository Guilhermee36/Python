import math

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = peso / math.pow(altura, 2)
print(" Seu IMC é: {} ".format(imc))

if imc < 20:
    print(" Você está abaixo do peso ideal")
elif imc >= 20 and imc < 25:
    print(" Você está no peso ideal")
elif imc >= 25 and imc < 30:
    print(" Você está com sobrepeso")
elif imc >= 30 and imc < 35:
    print(" Você está  obeso")
elif imc >= 40:
    print(" obesidade morbida")
    
    