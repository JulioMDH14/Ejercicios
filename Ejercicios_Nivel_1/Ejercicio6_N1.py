asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

suspensas = []
for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota que has sacado en {asignatura}: "))
    if nota < 5:
        suspensas.append(asignatura)
print(f"Debes repetir las asignaturas de {suspensas}")