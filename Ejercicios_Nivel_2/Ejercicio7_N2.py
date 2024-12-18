diccionario = {}
lista_palabras = input("Introduce una lista de palabras con su traducción al ingles: ")

for p in lista_palabras.split(','):
    clave, valor = p.split(':')
    diccionario[clave] = valor
    
frase_es = input('Introduce una frase en español (se va a traducir al inglés): ')
for f in frase_es.split():
    if f in diccionario:
        print(diccionario[f], end=' ')
    else:
        print(f, end=' ')