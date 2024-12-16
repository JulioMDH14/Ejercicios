#9. Adivina un número (Avanzado)

from random import *
aleatorio = randint(1,100);
intentos = 1;
while True:
    numero = int(input('Introduce un número: '))
    if numero == aleatorio:
        print('Has adivinado el número aleatorio!!')
        break
    elif numero < aleatorio:
        print('El número que tienes que adiviar es mayor que el que has ingresado')
        intentos += 1
    else:
        print('El número que tienes que adiviar es menor que el que has ingresado')
        intentos += 1
        
print(f'Te han tomado {intentos} adivinar el número')
        

