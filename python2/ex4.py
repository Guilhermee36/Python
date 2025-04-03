NumNotas = float(input("Digite o número de notas: "))
Nota  = 0
Soma  = 0
media = 0  
cont = 0

while cont < NumNotas:
    Nota = float(input("Digite a nota: "))
    Soma = Soma + Nota
    cont = cont + 1

media = Soma / NumNotas
if media >= 6 :
    print("aluno aprovado com a média: {} ".format(media))

else:
    print("aluno reprovado com a média: {} ".format(media))    