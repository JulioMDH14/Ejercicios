#10. Juego de «Piedra, papel o tijera»

import random

def elegirOpcionOrdenador():
    opciones = ["piedra","papel","tijeras"]
    eleccion = random.choice(opciones)
    return eleccion

def ganadorPartida(usuario, ordenador):
    if usuario == ordenador:
        print('EMPATE!!')
    elif (
        (usuario == "piedra" and ordenador == "tijera") or
        (usuario == "papel" and ordenador == "piedra") or
        (usuario == "tijera" and ordenador == "papel")
    ):
        print('Has ganado!!')
    else:
        print('Ha ganado el ordenador')

while True:
    eleccionUsuario = input('Escoge una opción entre piedra, papel o tijeras: ').lower()
    if eleccionUsuario not in ["piedra","papel","tijeras"]:
        print('Esa no es una opcion, escoge una válida')
        continue
    ordenador = elegirOpcionOrdenador()
    resultado = ganadorPartida(eleccionUsuario,ordenador)
    
    repetir = input("¿Quieres repetir la partida? (Si/NO): ")
    if repetir.lower() != "si":
        break
