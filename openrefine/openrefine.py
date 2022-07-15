# Fragmentos de código para transformaciones en Open Refine
## Código en Python/Jython

## Quitar espacios en blanco (para códigos)

return value.replace(" ","")

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
