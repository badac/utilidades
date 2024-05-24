# Fragmentos de código para transformaciones en Open Refine
## Código en Python/Jython

## Quitar espacios en blanco (para códigos)
# Esto puede ser hecho con Edit cells > Common transforms > Trim leading and trailing whitespace

return value.replace(" ","")

## Reemplazar texto, soportando acentos y caracteres ES
return value.replace('MMC', 'María Mercedes Carranza'.decode('latin-1'))

## Concatenar dos columnas ##
## Esto también puede ser hecho con "Join Columns"

value = cells['Column 1']['value'] +  cells['Column 2']['value']
return value

## Generar ruta a partir de codigo ##
#un codigo cualquiera
cod = 'ERV_M_CA22_DOC007'
#lo dividimos en sus partes
parts = cod.split('_')

#para generar el nombre de cada carpeta, unimos con un '_' 
#cada parte con las partes anteriores de la lista 
#luego se pega cada nombre de carpeta con in /
#para generar ruta recursiva a partir de codigo

path = "/".join(["_".join(parts[:index+1]) for index, part in enumerate(parts)])

print(path)
#Imprime: 'ERV/ERV_M/ERV_M_CA22/ERV_M_CA22_DOC007'

#Verificar si una ruta existe
#value contiene la ruta a verificar
#este código retorna un 1 si existe y un 0 si no existe
import os
return os.path.exists(value)
