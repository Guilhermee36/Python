contador = 0
soma = 0
resp = "S"

while resp == "S" or resp == "s":
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja continuar? [S/N] ")


    if resp == "N" or resp == "n":
        print("Vc escolheu parar!")
        print("A soma dos números é: ", soma)
        print("A média dos números é: ", soma / contador)
    else:
        print("Vc escolheu continuar!")
