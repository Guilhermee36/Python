contador = 0
soma = 0
resp = "S"

while resp == "S" or resp == "s":
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja continuar? [S/N] ")

media = soma / contador
print("A media dos números é: ", soma)
