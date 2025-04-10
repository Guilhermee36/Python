
print("==========================================")
print("          TIPOS DE DIÁRIAS DISPONÍVEIS")
print("==========================================")
print("S - Simples: R$ 255.50 por diária")
print("D - Dupla:   R$ 305.50 por diária")
print("T - Tripla:  R$ 355.50 por diária")
print("==========================================\n")


Tipodiaria = input("Digite o tipo de diária (S - Simples, D - Dupla, T - Triplo): ")
Desconto = float(input("Digite o desconto em pocentagem %: "))

if Tipodiaria == "S" or Tipodiaria == "s":
    print("\nO valor da diária é (simples): R$ 255.50")
    print("\nDeseja continuar? (S/N)")
    continuar = input()
    if continuar == "S" or continuar == "s":
        print("Você escolheu continuar")
        quantidadeDiaria = int(input("Digite a quantidade de diárias: "))
        valorDiaria =  quantidadeDiaria * (255.50 * (1 - Desconto / 100))
        print("O valor total da diária é: R$", valorDiaria)
    else:
        print("Você escolheu não continuar")

elif Tipodiaria == "D" or Tipodiaria == "d":
    print("\nO valor da diária é (dupla): R$ 305.50")
    print("\nDeseja continuar? (S/N)")
    continuar = input()
    if continuar == "S" or continuar == "s":
        print("Você escolheu continuar")
        quantidadeDiaria = int(input("Digite a quantidade de diárias: "))
        valorDiaria = quantidadeDiaria * (305.50 * (1 - Desconto / 100))
        print("O valor total da diária é: R$", valorDiaria)
    else:
        print("Você escolheu não continuar")
        
elif Tipodiaria == "T" or Tipodiaria == "t":
    print("O valor da diária é (triple): R$ 355.50")
    print("\nDeseja continuar? (S/N)")
    continuar = input()
    if continuar == "S" or continuar == "s":
        print("Você escolheu continuar")
        quantidadeDiaria = int(input("Digite a quantidade de diárias: "))
        valorDiaria =  quantidadeDiaria * (355.50 * (1 - Desconto / 100))
        print("O valor total da diária é: R$", valorDiaria)
    else:
        print("Você escolheu não continuar")

else:
    print("Tipo de diária inválido. Por favor, escolha 'S' para Simples, 'D' para Dupla ou 'T' Para tripla.")