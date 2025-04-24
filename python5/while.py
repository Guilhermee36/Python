contador = 1
while contador <= 10:
    print("\nAluno %d" %(contador))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(" O aluno %d tem média: %.2f" %(contador, media))
    contador = contador + 1