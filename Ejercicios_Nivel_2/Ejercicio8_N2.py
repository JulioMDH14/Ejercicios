facturas = {}
cobrado = 0
pago_pendiente = 0
opcion = ""
while opcion != 'T':
    if opcion == 'A':
        numero_factura = input("Introduce el número de la factura:")
        valor = float(input("¿Cuanto ha costado la factura? "))
        facturas[numero_factura] = valor
        pago_pendiente = pago_pendiente + valor
    if opcion == 'P':
        numero_factura = input("Introduce el número de la factura:")
        valor = facturas.pop(numero_factura,0)
        cobrado = cobrado + valor
        pago_pendiente = pago_pendiente - valor
    print('Pago recaudado:', cobrado)
    print('Pagos pendientes de cobro: ', pago_pendiente)
    opcion = input("¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?")