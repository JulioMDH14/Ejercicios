asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

asignaturas_repetir = []

for asignatura in asignaturas:
    nota = float(input(f"¿Que nota has sacado en {asignatura}?: "))
    if nota < 5:
        asignaturas_repetir.append(asignatura)

if asignaturas_repetir:
    print("Las asignaturas que tienes que repetir son:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print("Has aprobado todo!!")
