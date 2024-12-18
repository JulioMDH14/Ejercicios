clientes = {}
opcion = input("Escoge una opción (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar ")
while opcion != '6':
    if opcion == '1':
        nif = input("Introduce tu NIF: ")
        nombre = input("Introduce tu nombre: ")
        edad = int(input("Introduce tu edad: "))
        telefono = int(input("Introduce tu número de teléfono: "))
        correo = input("Introduce tu correo electrónico: ")
        preferente = input("¿Eres un cliente preferente o no?")
        informacion = {"nombre":nombre,"edad":edad,"telefono":telefono,"correo":correo,"prefente":preferente}
        clientes[nif] = informacion
    if opcion == '2':
        nif = input("¿Cuál es tu NIF? ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("Ese NIF no existe")
    if opcion == '3':
        nif = input('Introduce tu NIF: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe un cliente que tenga ese nif', nif)   
    if opcion == '4':
        print('Lista de todos los clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de los clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])  

