import csv
#Le agregué al mismo archivo csv un encabezado, por eso trabajo con el mismo archivo del ejercicio 1
with open('Ejercicio_1.csv', 'r',encoding='utf-8') as csvfile:
    lector = csv.reader(csvfile)
    encabezados = next(lector)  # Lee la fila de encabezados
    print("Los encabezados son:", encabezados )
    for fila in lector:
        print(fila)