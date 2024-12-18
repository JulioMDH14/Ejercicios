asignaturas = {'Matemáticas': 6, 'Física': 4,'Química': 5}
total_creditos = 0
for a in asignaturas:
    print(f"{a} tiene {asignaturas[a]} créditos")
    total_creditos =  total_creditos + asignaturas[a]
    
print(f"Tienes un total de créditos de", total_creditos)