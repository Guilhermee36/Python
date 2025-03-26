import math

num = float(input("Digite um número real: "))
absoluto = math.fabs(num)
raiz = math.sqrt(num) if num >= 0 else "Número negativo não possui raiz quadrada real"
inteiro = math.trunc(num)
intBaixo = math.floor(num)
intCima = math.ceil(num)
fatorial = math.factorial(inteiro)

print("O valor absoluto é: {} \nA raiz quadrada do número é: {} \nO valor inteiro é: {}" .format(absoluto, raiz, inteiro))
print("O valor arredondado para baixo é: {} \nO valor arredondado para cima é: {} \n o valor do fatórial é {}" .format(intBaixo, intCima, fatorial))