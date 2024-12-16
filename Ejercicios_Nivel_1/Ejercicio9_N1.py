palabra = input("Introduce una palabra: ").lower()

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for vocal in palabra:
    if vocal == "a":
        contador_a = contador_a + 1
    elif vocal == "e":
        contador_e = contador_e + 1
    elif vocal == "i":
        contador_i = contador_i + 1
    elif vocal == "o":
        contador_o = contador_o + 1
    elif vocal == "u":
        contador_u = contador_u + 1

    
print(f"La vocal 'a' aparece {contador_a} veces.")
print(f"La vocal 'e' aparece {contador_e} veces.")
print(f"La vocal 'i' aparece {contador_i} veces.")
print(f"La vocal 'o' aparece {contador_o} veces.")
print(f"La vocal 'u' aparece {contador_u} veces.")