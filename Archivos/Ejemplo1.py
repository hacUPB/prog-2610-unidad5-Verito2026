fp = open(".\\Archivos\\Ejercicio_1.txt", "r", encoding="utf-8")
datos_1 = fp.readlines()
print(datos_1[0])

# datos_2 = fp.read(5)
# print("Segunda lectura:", datos_2)


# datos_3 = fp.read()
# print("Tercera lectura:",datos_3)
fp.close()

