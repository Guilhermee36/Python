media = float(input("Digite a média do aluno: "))
frequencia =  float(input("Digite o percentual da frequencia "))

if media < 6:
    print("Aluno reprovado por nota") 
else:
    if frequencia < 75:
        print("Aluno reprovado por falta")
        
    else:
        print("Aluno Aprovado!")
     
