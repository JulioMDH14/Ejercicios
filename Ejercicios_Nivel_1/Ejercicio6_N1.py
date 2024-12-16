asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

suspensas = []
for asignatura in asignaturas:
    try:
        nota = float(input(f"Introduce la nota que has sacado en {asignatura}: "))
        if nota < 5:
            suspensas.append(asignatura)
    except ValueError:
        print("Ese valor no es válido para las notas")
print(f"Debes repetir las asignaturas de {suspensas}")