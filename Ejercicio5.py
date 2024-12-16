ganadores = []
print("Introduce los números que han ganado la lotería: ")

for x in range(6):
    while True:
        try:
            numero = int(input(f"Boleto {x + 1}: "))
            if 1 <= numero <= 49:
                ganadores.append(numero)
                break
            else:
                print("Introduce otro número")
        except ValueError:
            print("ERROR: Introduce un número entero positivo")
print("Los ganadores son:")
print(ganadores)