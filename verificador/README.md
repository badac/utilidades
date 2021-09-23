# Verificador

Este script se usa para verificar el vínculo entre el código BADAC de un documento en una tabla y el archivo o conjunto de archivos que conforman el documento digitalizado.

## Requisitos

Para usar este script se debe tener acceso a la NAS del BADAC y haber montado la carpeta del fondo en el finder. (Cmd+K, connect to server)

Se debe tener una tabla de metadatos en formato CSV de un fondo, que debe tener una lista de códigos únicos o identificadores de cada documento.

La tabla de metadatos en formato CSV debe usar el caracter ```|``` como separador y debe haber sido guardada con la codificación "UTF-8"

El script ha sido probado con las versiones 2.7 y 3.7 de Python, pero se recomienda usar la 3.7

## Uso

Clonar o bajar el repositorio en el computador.

Copiar la tabla (archivo .csv) con los códigos en la carpeta ```datos/```.

Crear una copia del archivo de configuración ```config.json.template``` y cambiarle el nombre a ```config.json```

Editar los valores del archivo de configuración (ver sección configuración)

Desde la terminal, navegar a la carpeta ```utilidades/verificar``` y ejecutar

```bash
python verificar.py
```
### Generación de reportes

El script genera tres reportes cada vez que se ejecuta.  Un reporte de registros encontrados, un reporte de registros no encontrados y un reporte de registros que se encontraron, pero que hace falta los de calidad media.

Los reportes son tablas CSV que contienen el código verificado, la ruta generada a partir del código y el contenido de la carpeta de archivos en media calidad o el contenido de la carpeta del documento

El caracter separador de las tablas de los reportes es ```|```.

Los siguientes son los nombres de los reportes:

pero que falta generar las imágenes en calidad media y guardarlas en la carpeta ```MEDIA/```del documento.



## Configuración

La configuración del script se realiza editando el archivo config.json.  Si este archivo hace falta, o está mal configurado, el script fallará.

Los siguientes son los parámetros de configuración y sus funciones.

### Fondo

```json
"fondo": "/ruta/carpeta/contenedora/fondo"
```

Es la ruta a la carpeta contenedora de los archivos del fondo.  Usualmente esta carpeta se llama igual que la primera parte del código de los documentos del fondo:

Por ejemplo, el documento con el código pertenece al fondo __Luis Caballero__, cuya carpeta raíz es:
```
Volumes/FONDOS/Luis Caballero Holguín/LCH
```
La ruta de la configuración sería
```
/Volumes/FONDOS/Luis Caballero Holguín/
```
Es importante dejar un ```/``` al final de la ruta

### Tabla de entrada de datos


```json
  "input_table": "tabla.csv"
```

Nombre de archivo de la tabla de metadatos con los códigos a verificar.  Esta tabla debe venir en formato __.csv__, el carácter separador de las columnas debe ser ```|```(barra vertical) y debe estar guardado con la codificación __UTF-8__.  Usualmente este archivo se exporta desde _Excel_, _OpenRefine_ o cualquier otra herramienta de gestión de datos.


### Columna de ID o Código

```json
  "id_col": 0,
```

El número de la columna en la que se encuentra el código a verificar.  Es un número entero y se puede definir de la siguiente forma.

Se cuentan las columnas de izquierda a derecha, siendo la primera columna la número 0, hasta la que contiene el ID o código.  Usualmente esta columna se llama "ID", "Código" o "Código BADAC".

Ejemplo:

Si la primera columna contiene el código entonces es la 0:

```json
  "id_col": 0,
```

Si la segunda columna contienen el código entonces es la 1:

```json
  "id_col": 1,
```

Y así sucesivamente.

### Carpeta de imágenes en calidad MEDIA

```json
  "img_dir": "/MEDIA/",
```

Nombre de la carpeta en donde se encuentran las imágenes en calidad media para publicar.  Generalmente se llama ```/MEDIA/```.

En general no es necesario cambiar este valor.

### Carpeta de datos

```json
  "data_dir": "datos/",
```

Ruta a la carpeta que contiene la tabla de metadatos (el valor de ```input_table```). Debe ser una ruta relativa a la ubicación de ```verificar.py```.

Generalmente no hay que cambiar este valor.

### Carpeta de reportes

```json
"report_dir": "reportes/",
```

Ruta a la carpeta donde se guardarán los reportes generado por el script.  Debe ser una ruta relativa.

Generalmente no hay que cambiar este valor.

### Código redundante

El valor de esta configuración puede ser ```true```o ```false```.

Es el tipo de nombres de carpetas generadas a partir del código.

Una nomenclatura __redundante__ es cuando en el nombre de la carpeta se incluyen las partes del identificador anteriores:

Código:

```
MMC_PER_COR_1948_DOC001
```

Ruta:
```
MMC/MMC_PER/MMC_PER_COR/MMC_PER_COR_1948/MMC_PER_COR_1948_DOC001
```
En este caso la configuración es:

```json
"redundante": true
```

Una nomenclatura __no redundante__ es cuando el nombre de la carpeta sólo tiene la parte del código que le corresponde:

Código:

```
LCH_1980_1988_036
```

Ruta:

```
LCH/1980/1988/036/
```

En este caso la configuración es:

```json
"redundante": false
```

En general este parámetro no se cambia.
