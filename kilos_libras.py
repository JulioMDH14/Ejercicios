peso = float(input("¿Cuál es tu peso?"))
pregunta = input("¿(K)g ó (L)bs?").lower()

if pregunta == "k":
    peso_lbs = peso / 0.45
    print(f"Tu peso en Libras es {peso_lbs}")
elif pregunta == "l":
    peso_kg = peso * 0.45
    print(f"Tu peso en Kilos es {peso_kg}")
else:
    print('ERROR: Dato mal introducido')