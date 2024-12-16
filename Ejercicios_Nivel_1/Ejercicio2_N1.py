<<<<<<< HEAD
def ordena_positivos(lista):
    if lista == []:
        print("Esta lista está vacía")
        return lista
    else:
        for n in lista:
            if n > 0:
                lista.sort()
        return lista
            
lista = [1,235,65,3,24,6,4,6,3,7,2,76,8,3,2,6,8,434,24]
print(ordena_positivos(lista))
=======
def ordena_positivos(lista):
    if lista == []:
        print("Esta lista está vacía")
        return lista
    else:
        for n in lista:
            if n > 0:
                lista.sort()
        return lista
            
lista = [1,235,65,3,24,6,4,6,3,7,2,76,8,3,2,6,8,434,24]
print(ordena_positivos(lista))
>>>>>>> ca78edad6efc244e211ed8ca1d047490cd990974
