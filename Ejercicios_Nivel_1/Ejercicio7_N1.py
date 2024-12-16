import string
abecedario = []
abecedario_multiplos = []
for letra in string.ascii_lowercase:
    abecedario.append(letra)
for n in abecedario:
    if abecedario.index(n) % 3 == 0:
        abecedario_multiplos.append(n)
print(f"Las letras del abecedario multiplos de 3 son {abecedario_multiplos}")