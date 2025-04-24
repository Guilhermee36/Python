# Laço while com break
print("Laço WHILE com BREAK")
d = 0
while d < 5:
    d += 1
    print("O número do laço é: ", d)
    if int(d) == 5:
        break

print("-" * 30)  # Separador visual

# Laço FOR com BREAK
print("Laço FOR com BREAK")
for d in range(10):
    if int(d) == 5:
        break
    print("O número do laço é: ", d)

print("-" * 30)  # Separador visual

# Laço FOR com CONTINUE
print("Laço FOR com CONTINUE")
for d in range(10):
    if int(d) == 5:
        continue
    print("O número do laço é: ", d)

print("-" * 30)  # Separador visual