import csv
with open('Ejercicio_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)