media = float(input("Digite a média do aluno: "))
frequencia =  float(input("Digite o percentual da frequencia "))

if frequencia < 75:
    print("\n Aluno reprovado por falta ")
    
else:
    if media < 6:
        print("\n Aluno reprovado por nota")
        
    else:
        print("\nAluno aprovado por nota") 