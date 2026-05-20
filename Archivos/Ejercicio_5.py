import csv

with open('Ejercicio_5.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)

    # Encabezados
    escritor.writerow(['Materia', 'Nota', 'Estudiante'])

    # Datos
    escritor.writerow(['Cálculo',3.2, 'Camila'])
    escritor.writerow(['Estática', 1.0, 'Sebastian'])
    escritor.writerow(['Sistemas', 4.2, 'Pablo'])

print("Archivo CSV creado correctamente")