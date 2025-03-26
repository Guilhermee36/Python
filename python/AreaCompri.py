import math
raio = float(input("Digite o raio da crcunferencia em centimetros :"))

area = math.pi * (raio ** 2)
comprimento = 2 * math.pi * raio

print("O raio da circunferencia é: %.2fcm \n" % raio) 
print("A area da circunferencia é: %.2fcm \n" % area) 
print("O comprimento da cincunferencia é: %.2fcm" % comprimento)