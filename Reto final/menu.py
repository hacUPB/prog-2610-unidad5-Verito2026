from pathlib import Path
import matplotlib.pyplot as plt
conectores = [
    "de", "la", "el", "y", "que", "en", "un", "una", "los", "las",
    "a", "con", "por", "para", "del", "se", "al", "es", "mi", "me",
    "no", "lo", "más", "su", "sus", "tu", "te", "le", "les", "como",
    "pero", "si", "sí", "ya", "o", "u", "ha", "hay", "fue", "era",
    "ser", "son", "mis", "sin", "cuando", "había", "vez", "hasta"
]
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

        print("\n==============================")
        print("       SUBMENÚ 1")
        print("1. Ver resumen estadístico del texto")
        print("2. Generar gráfico de palabras frecuentes")
        print("3. Generar histograma de longitud de líneas")
        print("4. Volver al menú principal")
        print("==============================")

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
def resumen_txt():                                      #Funcion de la primera opción del submenú 1

    ruta_txt = input("Ingresa la ruta del archivo: ")

    try:

        with open(ruta_txt, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

        cantidad_lineas = len(lineas)                    #Cantidad de lineas

        texto = " ".join(lineas)                         # Unir todo el texto

        caracteres_con_espacios = len(texto)             # Caracteres con espacios

        # Caracteres sin espacios
        texto_sin_espacios = texto.replace(" ", "")
        texto_sin_espacios = texto_sin_espacios.replace("\n", "")
        caracteres_sin_espacios = len(texto_sin_espacios)

        palabras = texto.split()                          # Separar texto en palabras

        palabras_limpias = []

        # Limpiar palabras
        for palabra in palabras:

            palabra = palabra.lower()

            for signo in signos:
                palabra = palabra.replace(signo, "")

            # Quitar conectores
            if palabra not in conectores and palabra != "":
                palabras_limpias.append(palabra)

        # Contar frecuencia de palabras
        contador_palabras = {}

        for palabra in palabras_limpias:

            if palabra in contador_palabras:
                contador_palabras[palabra] += 1

            else:
                contador_palabras[palabra] = 1

        palabras_ordenadas = list(contador_palabras.items())           # Convertir diccionario a lista

        # Método burbuja
        for i in range(len(palabras_ordenadas)):

            for j in range(len(palabras_ordenadas) - 1):

                if palabras_ordenadas[j][1] < palabras_ordenadas[j + 1][1]:

                    temporal = palabras_ordenadas[j]

                    palabras_ordenadas[j] = palabras_ordenadas[j + 1]

                    palabras_ordenadas[j + 1] = temporal

        # Mostrar resultados
        print("\n==============================")
        print("   RESUMEN DEL TEXTO")
        print("==============================")

        print("Cantidad de líneas:",
              cantidad_lineas)

        print("Cantidad de palabras:",
              len(palabras_limpias))

        print("Caracteres con espacios:",
              caracteres_con_espacios)

        print("Caracteres sin espacios:",
              caracteres_sin_espacios)

        print("\nTop 5 palabras más repetidas:")

        for palabra, cantidad in palabras_ordenadas[:5]:

            print("-", palabra, ":", cantidad)

    except FileNotFoundError:

        print("No se encontró el archivo TXT")
def graficar_palabras_frecuentes():                     #Función de la segunda opción del submenú

    ruta_txt = input(
        "Ingresa la ruta COMPLETA del archivo .txt: "
    )

    try:

        with open(ruta_txt, "r", encoding="utf-8") as archivo:

            texto = archivo.read()

        palabras = texto.split()

        palabras_limpias = []

        # Limpiar palabras
        for palabra in palabras:

            palabra = palabra.lower()

            for signo in signos:
                palabra = palabra.replace(signo, "")

            if palabra not in conectores and palabra != "":
                palabras_limpias.append(palabra)

        # Contar frecuencia
        contador_palabras = {}

        for palabra in palabras_limpias:

            if palabra in contador_palabras:
                contador_palabras[palabra] += 1

            else:
                contador_palabras[palabra] = 1

        # Convertir a lista
        palabras_ordenadas = list(
            contador_palabras.items()
        )

        # Método burbuja
        for i in range(len(palabras_ordenadas)):

            for j in range(
                    len(palabras_ordenadas) - 1):

                if palabras_ordenadas[j][1] < palabras_ordenadas[j + 1][1]:

                    temporal = palabras_ordenadas[j]

                    palabras_ordenadas[j] = palabras_ordenadas[j + 1]

                    palabras_ordenadas[j + 1] = temporal

        # Top 10
        top_10 = palabras_ordenadas[:10]

        nombres = []
        frecuencias = []

        for palabra, cantidad in top_10:

            nombres.append(palabra)
            frecuencias.append(cantidad)

        # Crear carpeta outputs
        carpeta_output = Path("outputs")
        carpeta_output.mkdir(exist_ok=True)

        # Crear gráfica
        plt.figure(figsize=(8, 5))

        plt.barh(nombres, frecuencias)

        plt.title(
            "10 palabras más frecuentes en El gato negro"
        )

        plt.xlabel("Frecuencia")
        plt.ylabel("Palabras")

        plt.savefig(
            "outputs/palabras_frecuentes.png"
        )

        plt.show()

        print(
            "Gráfico guardado correctamente"
        )

    except FileNotFoundError:

        print("No se encontró el archivo TXT")
def graficar_longitud_lineas():                         #Función de la tercera opción del submenú

    ruta_txt = input(
        "Ingresa la ruta del archivo .txt: "
    )

    try:

        with open(ruta_txt, "r",
                  encoding="utf-8") as archivo:

            lineas = archivo.readlines()

        # Lista vacía
        longitudes = []

        # Recorrer líneas
        for linea in lineas:

            cantidad_caracteres = len(linea)

            longitudes.append(
                cantidad_caracteres
            )

        # Crear carpeta outputs
        carpeta_output = Path("outputs")
        carpeta_output.mkdir(
            exist_ok=True
        )

        # Crear histograma
        plt.figure(figsize=(8, 5))

        plt.hist(longitudes)

        plt.title(
            "Distribución de longitud de líneas"
        )

        plt.xlabel(
            "Cantidad de caracteres por línea"
        )

        plt.ylabel("Frecuencia")

        # Guardar imagen
        plt.savefig(
            "outputs/longitud_lineas.png"
        )

        plt.show()

        print(
            "Histograma guardado correctamente"
        )

    except FileNotFoundError:

        print(
            "No se encontró el archivo TXT"
        )

#Menú principal donde llamamos las funciones
print("==============================")
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
        print("Aquí irá la opción para analizar archivo CSV")

    elif opcion == 4:
        print("Programa finalizado")
        break
    else:
        print("Opción inválida")
    


       