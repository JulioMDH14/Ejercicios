#8. Factorial
numero = int(input('Introduce un número: '))
factorial = 1;
for n in range(1, numero+1):
    factorial = factorial * n
print(f"El factorial de {numero} es {factorial}")