# importa libreria para hacer peticiones http
import urllib2

#obtener la url del campo url
url  = None
try:
    url = cells['url']['value']
except KeyError:
    value  = 'KO'


# si existe la url
if url:

    try:
        #crear un objeto request
        request = urllib2.Request(url)
        #realizar la peticion y obtener la respuesta
        res = urllib2.urlopen(request)
        #leer el contenido de la respuesta
        content = res.read()
        #obtener el status code
        status = res.getcode()
        #si es 200 (OK)
        if status == 200:
            value = 'OK'
    # Si da error HTTP
    except urllib2.HTTPError as e:
        value = 'KO'

#retorna el valor
return value