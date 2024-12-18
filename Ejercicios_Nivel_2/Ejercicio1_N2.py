monedas = {'Euro':'€', 'Dolar':'$', 'Yen': '¥'}
pregunta = input('¿Escoge una divisa para una moneda? ').title()

if pregunta in monedas:
    print(f'La divisa {pregunta} si está en el diccionario')
else:
    print(f'La divisa {pregunta} no está en el diccionario')
