#3. Adivina un número (fácil)

numero_oculto = 14
pregunta = int(input('¿Cuál es el número oculto? '))
#Un intento
intento = 1
while intento != 0:
    if pregunta == numero_oculto:
        print('¡Has acertado!')
        break
    else:
        print('No has acertado')
    intento -= 1
