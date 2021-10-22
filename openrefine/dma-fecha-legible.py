## Crear fecha iso a partir de campos dd mm aaa
import re
import locale
import datetime

#locale.setlocale(locale.LC_ALL, '')
value = ''

#Expresión para detectar cifras
exp = re.compile('\d+')

#Extrae los valores de las celdas con componentes de fecha
aaaa = cells['aaaa publicacion']['value']
mm = cells['mm publicacion']['value']
dd = cells['dd publicacion']['value']

year = month = day = False

format = ''
## Condicionales para filtrar y concatenar los números
if  exp.match(aaaa):
    year = int(exp.findall(aaaa)[0])

if  exp.match(mm):
    month = int(exp.findall(mm)[0])

if  exp.match(dd):
    day = int(exp.findall(dd)[0])


if year and month and day:
    d = datetime.date(year, month, day)
    format = "%d de %B de %Y"
    value = d.strftime(format)

elif year and month and not day:
    d = datetime.date(year, month, 1)
    format = "%B de %Y"
    value = d.strftime(format)

elif year and not month and not day:
    d = datetime.date(year, 1, 1)
    format = "%Y"
    value = d.strftime(format)

elif not year and month and day:
    d = datetime.date(1, month, day)
    format = "%d de %B"
    value = d.strftime(format)


return value
