idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65: 
    print("eleitor obrigatório")
    
elif idade >= 16 and idade < 18 or idade > 65:
     print("eleitor facultativo")  
           
else:
    print("não eleitor")
