informacion = {}
while True:
    clave = input("¿Qué información quieres añadir (nombre, edad, direccion, etc)? ")
    valor = input("Introduce el valor: ")
    informacion[clave] = valor
    continuar = input("¿Quieres añadir más información (Si/No)? ").strip().lower()
    if continuar != 'si':
        break
