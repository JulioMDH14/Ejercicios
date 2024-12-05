#3. Adivina un número (fácil)

numero_oculto = 14
pregunta = int(input('¿Cuál es el número oculto? '))
acierto = True
#Intentos infinitos
while acierto:
    if pregunta == numero_oculto:
        acierto = True
        break;
    else:
        print('Sigue intentandolo!!')
if acierto == True:
    print('¡Has acertado!')
else:
    print('No has acertado')
