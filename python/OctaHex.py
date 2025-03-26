resp = input("voce deseja conervter de octa para hexa? (O/o) ou hexa para octa? (H/h) : ")

if resp == "O" or resp == "o":
    Nbin = int(input("escreva um numero octa para hexa : "))
    Nhex = ""
    while Nbin > 0:
        if Nbin % 16 < 10:
            Nhex = str(Nbin % 16) + Nhex
        else:
            Nhex = chr(55 + Nbin % 16) + Nhex
        Nbin = Nbin // 16
    print(Nhex)
    
    if resp == "H" or resp == "h":
        Nbin = int(input("escreva um numero hexadecimal para octa: "))
        Noct = ""
        while Nbin > 0:
            Noct = str(Nbin % 8) + Noct
            Nbin = Nbin // 8
        print(Noct)
