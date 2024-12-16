#3. Adivina un número (fácil)

numero_oculto = 14
acierto = True
#Intentos infinitos
while acierto == True:
    pregunta = int(input('¿Cuál es el número oculto? '))
    if pregunta == numero_oculto:
        acierto = True
        print('Has acertado!!')
        break;
    else:
<<<<<<< HEAD
        print('Sigue intentandolo!!')
=======
        print('Sigue intentandolo!!')
>>>>>>> 51c924ae2a85b86038f3449bb5eb4bf17ca1c668
