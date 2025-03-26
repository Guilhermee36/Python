resp = input("voce deseja converter de decimal para binário? (D/d) ou binário para decimal? (B/b) : ")
if resp == "D" or resp == "d":
    Nbin = int(input("escreva um numero decimal para binário   : "))
    Ndec = 0
    i = 0
    while Nbin > 0:
        Ndec = Ndec + (Nbin % 10) * 2**i
        Nbin = Nbin // 10
        i = i + 1
    print(Ndec)
elif resp == "B" or resp == "b":
    Ndec = int(input("escreva um numero binário para decimal : "))
    Nbin = ""
    while Ndec > 0:
        Nbin = str(Ndec % 2) + Nbin
        Ndec = Ndec // 2
    print(Nbin)

