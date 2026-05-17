import csv

with open('Ejercicio_4.csv', 'r', encoding='utf-8') as csvfile:
    lector = csv.DictReader(csvfile)

    for fila in lector:
        producto = fila['Producto']
        precio = float(fila['Precio'])
        cantidad = int(fila['Cantidad'])

        valor_total = precio * cantidad

        print(f'El valor total de {producto} en inventario es: {valor_total}')