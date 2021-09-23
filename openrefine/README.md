# Snippets OpenRefine

Los archivos en este directorio son fragmentos de código escritos en la sintaxis de ```Python/Jython 2.7``` y para ser usados en OpenRefine en transformaciones y otros procesos.

Estos archivos no son scripts autónomos ejecutables en un interprete de python (Ej. desde la terminal) y van a generar error si se intentan ejecutar como scripts. (Ej. Al ejecutar ```python openrefine.py``` en una terminal, va a generar error.)

## Uso

La función de cada fragmento está documentada en los comentarios del código.

Para usar el fragmento se debe copiar el código del script correspondiente a lo que se quiere hacer.

Pegar el código en el cuadro de diálogo correspondiente en OpenRefine, por ejemplo en el díalogo de la función ```Cells > Transform```.

Cambiar los valores necesarios.  Algunos fragmentos requieren cambiar algunas partes del código. Por ejemplo para concatenar valores de otras celdas en la celda transformada, se deben cambiar los nombres de las columnas en el código para referirse a las columnas correspondientes en la tabla sobre la que estamos trabajando:

Por ejemplo si el código extrae una fecha de una columna llamada ```Fecha publicacion aaaa```, en el código se debe referir esa columna así:

```python
cells['Fecha publicacion aaaa']['value']
```

El siguiente paso es ejecutar la acción (hacer click en OK en el diálogo de OpenRefine).
