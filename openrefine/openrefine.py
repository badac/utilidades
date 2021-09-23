# Fragmentos de código para transformaciones en Open Refine
## Código en Python/Jython

## Quitar espacios en blanco (para códigos)

return value.replace(" ","")

## Concatenar dos columnas
## Esto también puede ser hecho con "Join Columns"

value = cells['Column 1']['value'] +  cells['Column 2']['value']
return value
