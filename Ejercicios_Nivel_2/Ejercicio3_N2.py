frutas = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}

preguntaFruta = input("¿Que fruta quieres comprar? ").title()
preguntaKilos = float(input("¿Cuantos kilos quieres comprar? "))

if preguntaFruta in frutas:
    print(f"{preguntaFruta} vale", frutas[preguntaFruta] * preguntaKilos,"€")
else:
    print("Está fruta no está a la venta actualmente")