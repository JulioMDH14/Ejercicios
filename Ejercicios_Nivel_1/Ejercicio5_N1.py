ganadores = []
for n in range(6):
    try:
        numeros = int(input("Introduce los números ganadores de la loteria: "))
        ganadores.append(numeros)
    except ValueError:
        print("Debes introducir un entero positivo.")
ganadores.sort()
print("Los ganadores son: ")
print(ganadores, end=" ")