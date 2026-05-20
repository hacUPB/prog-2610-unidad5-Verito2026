# Documento de Análisis
## Estructura general de nuestro código
Nuestro código está organizado con un menú principal, donde el usuario puede escoger entre cuatro opciones: explorar un directorio, procesar archivos .txt, analizar archivos .csv o salir del programa.

Cada opción del menú llama una función diferente dependiendo de lo que el usuario quiera hacer. Además, las opciones de TXT y CSV tienen un submenú, porque dentro de ellas hay varias cosas que se pueden hacer.

Entonces, cuando el usuario escoge una opción del submenú, se llama otra función específica para esa tarea, por ejemplo mostrar estadísticas, buscar información o generar gráficos. De esta manera el código queda más organizado, porque cada función se encarga de una sola cosa y no toca repetir tanto código.
## 1. Explicación de los Datos Elegidos
Para probar el código que hicimos, elegimos tres archivos bien diferentes para ver si el programa de verdad servía tanto para analizar textos como para procesar tablas:

### Texto Narrativo (El_gato_negro.txt): 
Es el cuento completo de Edgar Allan Poe. Lo usamos para probar el submenú de texto, ver cuántas líneas tiene, limpiar los signos de puntuación y sacar el top de las palabras que el autor más repite a lo largo de la historia.

### Datos Climáticos (Clima_Colombia.csv): 
Este archivo tiene los datos de varios aeropuertos y estaciones de Colombia. Muestra información de la ubicación (como las coordenadas y la altura sobre el nivel del mar) y el tipo de clima que hace en cada mes del año.

### Datos Empresariales (Empresas_mas_grandes_Risaralda.csv):
 Es una tabla con información financiera de las empresas que más plata mueven en Risaralda (con datos de 2022 a 2024). Tiene columnas con el NIT, el nombre de la empresa, a qué sector pertenece, y los valores de sus ingresos, activos y pasivos.

 Es importante mencionar que los archivos csv fueron descargados de Datos Abiertos Colombia.

## 2. Conclusiones Reales del Análisis de los Gráficos
Después de correr el script y revisar los archivos que se guardaron en la carpeta outputs, sacamos estas tres conclusiones:

### Conclusión 1: Las palabras clave muestran la obsesión del protagonista
Al revisar el gráfico de barras horizontales, nos dimos cuenta de que después de quitar todas las palabras de la lista de conectores (como "de", "la", "que"), las que más se repiten con mucha diferencia son "gato", "casa" y "esposa". Esto tiene todo el sentido con la historia del cuento, porque muestra de forma matemática cómo la trama de terror psicológico de Poe gira completamente en torno a la obsesión del tipo con su mascota, los problemas que tenía en su casa y el asesinato de la esposa.

### Conclusión 2: El comercio y los servicios dominan la economía de Risaralda
Cuando generamos el gráfico de pastel usando la columna de MACROSECTOR del archivo de las empresas, se ve clarísimo que la gran mayoría de la torta se la llevan los sectores de Comercio y Servicios. Los sectores de manufactura (fábricas) o el agro ocupan un espacio súper chiquito. Esto nos permite concluir que la economía de las empresas más grandes de esa región depende casi toda del comercio y de prestar servicios, y no tanto de producir o fabricar cosas.

### Conclusión 3: Unas pocas empresas se quedan con casi toda la plata
Viendo el gráfico de dispersión que cruza los activos con los ingresos, o el gráfico de líneas, se nota un comportamiento muy raro: la gran mayoría de las empresas están amontonadas abajo porque tienen ingresos "normales", pero hay un par de puntos que se disparan lejísimos en la gráfica. Esto nos dice que el mercado en Risaralda está muy concentrado; hay un grupito mini de empresas gigantes que dominan casi toda la plata de la región, mientras que el resto de las empresas del ranking juegan en un nivel mucho más bajo.