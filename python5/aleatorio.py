from random import *

num = randint(0, 10)
i = 0
controle = 0

while (controle == 0):
    i += 1
    X = int(input("Digite um número ineiro: "))
    if num == X:
        print("Você acertou o número em {} tentativas".format(i))
        controle = 1
    elif num > X:
        print("O número é maior")
    else:
        print("O número é menor")
        