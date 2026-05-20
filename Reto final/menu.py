from pathlib import Path
import matplotlib.pyplot as plt
import csv
conectores = ["de", "la", "el", "y", "que", "en", "un", "una", "los", "las", "a", "con", "por", "para", "del", "se", "al", "es", "mi", "me", "no", "lo", "más", "su", "sus", "tu", "te", "le", "les", "como", "pero", "si", "sí", "ya", "o", "u", "ha", "hay", "fue", "era", "ser", "son", "mis", "sin", "cuando", "había", "vez", "hasta"]
signos = [".", ",", ";", ":", "¿", "?", "¡", "!", '"', "(", ")", "-", "_", "\n"]
def explorar_directorio():                              #Funcion para la primera opción menu principal
    ruta = input("Ingrese la ruta de la carpeta: ")
    carpeta = Path(ruta)
    print("\nArchivos encontrados:\n")
    for archivo in carpeta.iterdir():

        if archivo.suffix == ".txt" or archivo.suffix == ".csv":
            print(archivo.name)
def menu_1():                                           #Función de la segunda opción del menú principal
    while True:

        print("\nSUBMENÚ 1")
        print("1. Ver resumen estadístico del texto")
        print("2. Generar gráfico de palabras frecuentes")
        print("3. Generar histograma de longitud de líneas")
        print("4. Volver al menú principal")
        
        opcion_txt = int(input("\nSeleccione una opción: "))

        if opcion_txt == 1:
            resumen_txt()

        elif opcion_txt == 2:
            graficar_palabras_frecuentes()

        elif opcion_txt == 3:
            graficar_longitud_lineas()
            
        elif opcion_txt == 4:
            print("Volviendo al menú principal...")
            break
def procesar_palabras(texto):                           #Funcion para palabras
    
    palabras = texto.split()

    palabras_limpias = []                               #Creamos lista vacía

    # Limpiar palabras
    for palabra in palabras:

        palabra = palabra.lower()                       #Convertimos todo a minusculas

        for signo in signos:
            palabra = palabra.replace(signo, "")       #Reemplazamos signos(lista al inicio) por nada, se elimina

        if palabra not in conectores and palabra != "":    #Sipalabra no es un conector y no quedó vacía, lo guardamos en la lista palabras_limpias
            palabras_limpias.append(palabra)

    # Contar frecuencia
    contador_palabras = {}                               #Diccionario que almacena palabra=cantidad de veces que se repite

    for palabra in palabras_limpias:                     #Recorremos la lista palabras_limpias

        if palabra in contador_palabras:                 #Verificamos si la palabra ya está en el diccionario
            contador_palabras[palabra] += 1              

        else:
            contador_palabras[palabra] = 1

    palabras_ordenadas = list(contador_palabras.items())

    # Método burbuja
    for i in range(len(palabras_ordenadas)):

        for j in range(len(palabras_ordenadas) - 1):

            if palabras_ordenadas[j][1] < palabras_ordenadas[j + 1][1]:

                temporal = palabras_ordenadas[j]

                palabras_ordenadas[j] = palabras_ordenadas[j + 1]

                palabras_ordenadas[j + 1] = temporal

    return palabras_limpias, palabras_ordenadas
def resumen_txt():                                      #Función de la primera opción del submenú 1

    ruta_txt = input("Ingresa la ruta del archivo: ")

    try:

        with open(ruta_txt, "r", encoding="utf-8") as archivo:         #Abrimos el archivo

            lineas = archivo.readlines()                               #Lee todas las lineas y devuelve una lista

        cantidad_lineas = len(lineas)                                  #Cantidad de lineas

        texto = " ".join(lineas)                                       #unimos todo en un solo texto corrido

        caracteres_con_espacios = len(texto)                           #Cuenta los caracteres incluyendo espacios

        texto_sin_espacios = texto.replace(" ", "")                   #Quitamos los espacios
        texto_sin_espacios = texto_sin_espacios.replace("\n", "")      #Quitamos los saltos de linea

        caracteres_sin_espacios = len(texto_sin_espacios)             #Cuenta el texto sin espacio y saltos de linea

        palabras_limpias, palabras_ordenadas = procesar_palabras(texto)

        print("\nRESUMEN DEL TEXTO")

        print("Cantidad de líneas:", cantidad_lineas)
        print("Cantidad de palabras:", len(palabras_limpias))
        print("Caracteres con espacios:", caracteres_con_espacios)
        print("Caracteres sin espacios:", caracteres_sin_espacios)

        print("\nTop 5 palabras más repetidas:")

        for palabra, cantidad in palabras_ordenadas[:5]:     #Le decimos que solo queremos las 5 primeras

            print("-", palabra, ":", cantidad)

    except FileNotFoundError:

        print("No se encontró el archivo TXT")
def graficar_palabras_frecuentes():                     #Función de la segunda opción del submenú 1

    ruta_txt = input("Ingresa la ruta del archivo .txt: ")

    try:

        with open(ruta_txt, "r", encoding="utf-8") as archivo:

            texto = archivo.read()

        palabras_limpias, palabras_ordenadas = procesar_palabras(texto)

        top_10 = palabras_ordenadas[:10]

        nombres = []
        frecuencias = []

        for palabra, cantidad in top_10:

            nombres.append(palabra)
            frecuencias.append(cantidad)

        carpeta_output = Path("outputs")
        carpeta_output.mkdir(exist_ok=True)

        plt.figure(figsize=(8, 5))

        plt.barh(nombres, frecuencias)

        plt.title("10 palabras más frecuentes")
        plt.xlabel("Frecuencia")
        plt.ylabel("Palabras")

        plt.savefig("outputs/palabras_frecuentes.png")

        plt.show()

        print("Gráfico guardado correctamente")

    except FileNotFoundError:

        print("No se encontró el archivo TXT")
def graficar_longitud_lineas():                         #Función de la tercera opción del submenú

    ruta_txt = input("Ingresa la ruta del archivo .txt: ")

    try:

        with open(ruta_txt, "r",encoding="utf-8") as archivo:

            lineas = archivo.readlines()

        # Lista vacía
        longitudes = []

        # Recorrer líneas
        for linea in lineas:

            cantidad_caracteres = len(linea)

            longitudes.append(cantidad_caracteres)

        # Crear carpeta outputs
        carpeta_output = Path("outputs")
        carpeta_output.mkdir(exist_ok=True)

        # Crear histograma
        plt.figure(figsize=(8, 5))

        plt.hist(longitudes)

        plt.title("Distribución de longitud de líneas")

        plt.xlabel("Cantidad de caracteres por línea")

        plt.ylabel("Frecuencia")

        # Guardar imagen
        plt.savefig("outputs/longitud_lineas.png")

        plt.show()

        print("Histograma guardado correctamente")

    except FileNotFoundError:

        print("No se encontró el archivo TXT")
def menu_2():                                           #Función de la tercera opción del menú principal

    while True:

        print("\nSUBMENÚ CSV")
        print("1. Vista previa de datos")
        print("2. Estadísticas descriptivas")
        print("3. Gráfico de líneas")
        print("4. Gráfico de pastel")
        print("5. Gráfico de dispersión")
        print("6. Volver al menú principal")

        opcion_csv = int(input("\nSeleccione una opción: "))

        if opcion_csv == 1:
            vista_previa_csv()

        elif opcion_csv == 2:
            estadisticas_csv()

        elif opcion_csv == 3:
            grafico_lineas_csv()

        elif opcion_csv == 4:
            grafico_pastel_csv()
        elif opcion_csv == 5:
            grafico_dispersion_csv()

        elif opcion_csv == 6:
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción inválida")
def vista_previa_csv():                                 #Función de la primera opción del submenú 2

    ruta_csv = input("Ingresa la ruta del archivo CSV: ")

    try:

        with open(ruta_csv,"r",encoding="utf-8") as archivo:

            lector = csv.reader(archivo)
            datos = list(lector)

        print("\nPRIMERAS 10 FILAS")

        for fila in datos[:10]:

            print(fila)


        print("\nÚLTIMAS 5 FILAS")

        for fila in datos[-5:]:

            print(fila)

    except FileNotFoundError:

        print("No se encontró el archivo CSV")
def estadisticas_csv():                                 #Función de la segunda opción del submenú 2

    ruta_csv = input("Ingresa la ruta del archivo CSV: ")

    try:

        with open(ruta_csv, "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)
            datos = list(lector)

        encabezados = datos[0]

        print("\nColumnas disponibles:")

        for encabezado in encabezados:
            print("-", encabezado)

        columna = input("Ingrese el nombre de la columna numérica: ")

        indice = encabezados.index(columna)

        valores = []

        for fila in datos[1:]:

            if fila[indice] != "":

                try:
                    valores.append(float(fila[indice]))

                except ValueError:
                    pass

        promedio = sum(valores) / len(valores)

        valores.sort()

        if len(valores) % 2 == 0:
            mediana = (valores[len(valores)//2 - 1] + valores[len(valores)//2]) / 2
        else:
            mediana = valores[len(valores)//2]

        print("\nTotal registros válidos:", len(valores))
        print("Promedio:", promedio)
        print("Mediana:", mediana)
        print("Máximo:", max(valores))
        print("Mínimo:", min(valores))

    except FileNotFoundError:

        print("No se encontró el archivo CSV")
def grafico_lineas_csv():                               #Función de la tercera opción del submenú 2

    ruta_csv = input("Ingresa la ruta del archivo CSV: ")

    try:

        with open(ruta_csv, "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)
            datos = list(lector)

        encabezados = datos[0]

        print("\nColumnas disponibles:")

        for encabezado in encabezados:
            print("-", encabezado)

        columna_x = input(
            "Ingrese el nombre de la columna para el eje X: "
        )

        columna_y = input(
            "Ingrese el nombre de la columna para el eje Y: "
        )

        indice_x = encabezados.index(columna_x)
        indice_y = encabezados.index(columna_y)

        valores_x = []
        valores_y = []

        for fila in datos[1:]:

            if fila[indice_x] != "" and fila[indice_y] != "":

                try:

                    y = fila[indice_y].replace(",", ".")

                    valores_x.append(fila[indice_x])
                    valores_y.append(float(y))

                except ValueError:
                    pass

        plt.figure(figsize=(8, 5))

        plt.plot(valores_x, valores_y)

        plt.title("Evolución temporal")
        plt.xlabel(columna_x)
        plt.ylabel(columna_y)

        plt.xticks(rotation=45)

        carpeta_output = Path("outputs")
        carpeta_output.mkdir(exist_ok=True)

        plt.savefig(
            "outputs/grafico_lineas.png"
        )

        plt.show()

        print("Gráfico guardado correctamente")

    except FileNotFoundError:

        print("No se encontró el archivo CSV")
def grafico_pastel_csv():                               #Función de la cuarta opcion del submenú 2

    ruta_csv = input("Ingresa la ruta del archivo CSV: ")

    try:

        with open(ruta_csv, "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)
            datos = list(lector)

        encabezados = datos[0]

        print("\nColumnas disponibles:")

        for encabezado in encabezados:
            print("-", encabezado)

        columna = input("Ingrese el nombre de la columna categórica: ")

        indice = encabezados.index(columna)

        categorias = {}

        for fila in datos[1:]:

            if fila[indice] != "":

                valor = fila[indice]

                if valor in categorias:
                    categorias[valor] += 1

                else:
                    categorias[valor] = 1

        nombres = list(categorias.keys())
        cantidades = list(categorias.values())

        plt.figure(figsize=(8,5))

        plt.pie(cantidades, labels=nombres, autopct="%1.1f%%")

        plt.title("Comparación categórica")

        carpeta_output = Path("outputs")
        carpeta_output.mkdir(exist_ok=True)

        plt.savefig("outputs/grafico_pastel.png")

        plt.show()

        print("Gráfico guardado correctamente")

    except FileNotFoundError:

        print("No se encontró el archivo CSV")
def grafico_dispersion_csv():

    ruta_csv = input("Ingresa la ruta del archivo CSV: ")

    try:

        with open(ruta_csv, "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)
            datos = list(lector)

        encabezados = datos[0]

        print("\nColumnas disponibles:")

        for encabezado in encabezados:
            print("-", encabezado)

        columna_x = input("Ingrese la primera columna numérica: ")
        columna_y = input("Ingrese la segunda columna numérica: ")

        indice_x = encabezados.index(columna_x)
        indice_y = encabezados.index(columna_y)

        valores_x = []
        valores_y = []

        for fila in datos[1:]:

            if fila[indice_x] != "" and fila[indice_y] != "":

                try:
                    # REEMPLAZOS BÁSICOS: Quitamos el $ y los puntos de miles para que float() funcione
                    texto_x = fila[indice_x].replace("$", "").replace(".", "")
                    texto_y = fila[indice_y].replace("$", "").replace(".", "")

                    valores_x.append(float(texto_x))
                    valores_y.append(float(texto_y))

                except ValueError:
                    pass

        plt.figure(figsize=(8,5))

        plt.scatter(valores_x, valores_y)

        plt.title("Correlación de variables")
        plt.xlabel(columna_x)
        plt.ylabel(columna_y)

        carpeta_output = Path("outputs")
        carpeta_output.mkdir(exist_ok=True)

        plt.savefig("outputs/grafico_dispersion.png")

        plt.show()

        print("Gráfico guardado correctamente")

    except FileNotFoundError:

        print("No se encontró el archivo CSV")
#Menú principal donde llamamos las funciones
print("Reto unidad 5")
while True:
    print("\nSelecciona una opción del menú")
    print("1. Explorar directorio")
    print("2. Procesar archivo .txt")
    print("3. Analizar archivo .csv")
    print("4. Salir")

    opcion=int(input("\n ¿Qué opción deseas elegir?:"))
    if opcion==1:
        explorar_directorio()                           #Llamamos la función de la opción 1
    elif opcion==2:
        menu_1()                                        #Llamamos la función de la opción 2, y se despliega el submenú 1
    elif opcion == 3:
        menu_2()                                        #Llamamos la función de la opción 3, y se despliega el submenú 2

    elif opcion == 4:
        print("Programa finalizado")
        break
    else:
        print("Opción inválida")
    


       