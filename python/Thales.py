import math
comprimento = float(input("Digit o comprimento da sombra:"))
angulo = float(input("Digite o angulo em graus:"))
altura = math.tan(math.radians(angulo)) * comprimento

print ("A altura do objeto é: %.2f" % altura)
