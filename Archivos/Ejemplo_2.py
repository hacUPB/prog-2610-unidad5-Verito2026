fp = open(".\\Archivos\\Texto_aleatorio.txt", "r", encoding="utf-8")
lista = fp.readlines()
fp.close()
print (lista)

for linea in lista:
    print(linea[0])
