nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección: ")
telefono = int(input("Introduce tu número de teléfono: "))

datos = {'Nombre':nombre,'Edad':edad,'Direccion':direccion,'Telefono':telefono}

print(f"{datos['Nombre']} tiene {datos['Edad']} años, vive en {datos['Direccion']} y su número de teléfono es {datos['Telefono']}")