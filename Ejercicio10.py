#10. Juego de «Piedra, papel o tijera»

import random

def elegirOpcionOrdenador():
    opciones = ["piedra","papel","tijeras"]
    eleccion = random.choice(opciones)
    return eleccion

