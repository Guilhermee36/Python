while True:  
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Vai tirar sua CNH!")
        break  
    else:
        print("\nVocê ainda não pode tirar sua CNH!")
