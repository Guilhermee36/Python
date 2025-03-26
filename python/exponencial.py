import math

base = float(input("digite o valor da base: "))
expoente = float(input("digite o valor do expoente: "))
valor = math.pow(base, expoente)

print("o valor da exponencial é {}".format(valor))
print("o valor da exponencial é %.2f" % valor)
