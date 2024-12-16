#3. Adivina un número (fácil)

numero_oculto = 14


#10 intentos
intento = 10
while intento != 0:
    pregunta = int(input('¿Cuál es el número oculto? '))
    if pregunta == numero_oculto:
        print('¡Has acertado!')
        break
    else:
        print('No has acertado')
        intento -= 1