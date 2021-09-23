## Crear fecha iso a partir de campos dd mm aaa
import re
#Expresión para detectar cifras
exp = re.compile('\d+')

#Extrae los valores de las celdas con componentes de fecha
aaaa = cells['aaaa publicacion']['value']
mm = cells['mm publicacion']['value']
dd = cells['dd publicacion']['value']

## Condicionales para filtrar y concatenar los números
if  exp.match(aaaa):
    value = exp.findall(aaaa)[0]
if  exp.match(mm):
    value = value + '-' + exp.findall(mm)[0]
if  exp.match(dd):
    value = value + '-' + exp.findall(dd)[0]

return value
