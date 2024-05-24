## Crear fecha iso a partir de campos dd mm aaa
import re
#Expresión para detectar cifras
exp = re.compile('\d+')

#Extrae los valores de las celdas con componentes de fecha
aaaa = cells['aaaa']['value']
mm = cells['mm']['value']
dd = cells['dd']['value']

#variable nueva para la fecha
fecha = ''

## Condicionales para filtrar, formatear y concatenar los números
if  exp.match(aaaa):
    fecha = exp.findall(aaaa)[0]
if  exp.match(mm):
    fecha = fecha + '-' + exp.findall(mm)[0].zfill(2)
if  exp.match(dd):
    fecha = fecha + '-' + exp.findall(dd)[0].zfill(2)

return fecha
