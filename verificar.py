#!/usr/bin/python
# -*- coding: latin-1 -*-

#Este script se usa como punto de partida para la compilación de fondos y #colecciones del BADAC

#Tiene principalmente tres funciones

#1: Cargar una tabla de datos, construir rutas a los directorios con archivos#!/usr/bin/python
# -*- coding: latin-1 -*-

#Este script se usa como punto de partida para la compilación de fondos y #colecciones del BADAC

#Tiene principalmente tres funciones

#1: Cargar una tabla de datos, construir rutas a los directorios con archivos
#del fondo, usando metadatos de la tabla,usualmente un id o un código
#único de un registro)

#2: Verificar que el archivo o archivos existen en la rutas y copiarlos a la
#carpeta de compilación, y generar reportes de los archivos encontrados o
#faltantes

#3: Agregar a la tabla de datos la ruta al archivo y la url pública donde se
#alojará la compilación
#
#Autor: Camilo Martinez (gemartin@uniandes.edu.co)


import sys, os, getopt
import csv
import datetime
from shutil import copyfile

#Tabla csv de entrada
input_table = "MT-CUA.csv"

#ruta a la carpeta del fondo.
fondo = "/Volumes/Marta_Traba/"

#ruta de la carpeta de archivos, relativa a la unidad documental
img_dir = "/MEDIA/"

#Nombre de la tabla de entrada, sin la extensión
input_fname = input_table[:-4]

#Folder de datos de entrada
data_dir = "datos/"

#Folder de reportes
report_dir = "reportes/"

#Ruta a la tabla
input_path = "datos/" + input_table

d = datetime.datetime.now()
timestamp = d.strftime("%Y-%m-%dT%H%M%S")

# Archivos de salida para los reportes
missing_report_table = report_dir + "faltantes_" + input_fname + "_"  + timestamp + ".csv"
found_report_table = report_dir + "encontradas_" + input_fname + "_"  + timestamp + ".csv"
nomedia_report_table = report_dir + "sin-media_" + input_fname + "_"  + timestamp + ".csv"

#un simple contador para los items encontrados
count = 0

# Número de la columna de ID o Código.
# Comenzando a contar desde cero.

id_col = 1

#Iteración sobre la tabla de entrada.
with open(input_path, 'r') as csvfile, open(missing_report_table, 'w') as missing_report_file, open(found_report_table, 'w') as found_report_file, open(nomedia_report_table, 'w') as nomedia_report_file:
    #objeto lector de la tabla de entrada
    tablereader = csv.reader(csvfile, delimiter='|', quotechar='"')

    #Objeto escritor de la tabla de reporte de faltatnes
    missing_reportwriter = csv.writer(missing_report_file, delimiter='|', quotechar='"')

    #Objeto escritor de la tabla de reporte de encontrados
    found_reportwriter = csv.writer(found_report_file, delimiter='|', quotechar='"')

    nomedia_reportwriter = csv.writer(nomedia_report_file, delimiter='|', quotechar='"')

    #encabezados de las tablas de reporte
    missing_reportwriter.writerow(['id','ruta'])
    found_reportwriter.writerow(['id','ruta', 'contenido'])
    nomedia_reportwriter.writerow(['id','ruta', 'contenido'])


    #Extraer los encabezados de la tabla de entrada
    first_row = next(tablereader)

    #Agregar nuevas columnas
    first_row = first_row + ['files', 'urls']
    print(first_row)


    #Proceso de la fila o registro
    for row in tablereader:
        #print(len(row))

        id = row[id_col] #celda donde se encuentra el id

        print(id)

        parts = id.split('_')

        directories = ["_".join(parts[:index + 1]) for index in range(len(parts))]
        print(directories)

        path_part = "/".join(directories)


        #para verificar la existencia de la carpeta
        path = fondo  + path_part

        #para escanear la carpeta con las imágenes
        path_img = fondo + path_part + img_dir

        print("ruta documento: " + str(path))
        print("ruta media: " + str(path_img))

        #Se verifica la existencia de la carpeta de la unidad documental
        #y de la carpeta de archivos
        #if(os.path.exists(path) and os.path.exists(path_img)):
        if(os.path.exists(path)):
            print("Existe la ruta")
            #escribir nueva entrada en el reporte de encontradas
            found_report_row = [id, path]
            found_reportwriter.writerow(found_report_row)
            document_contents = os.listdir(path)
            #Si existe la carpeta de archivos y contiene archivos
            if(os.path.exists(path_img) and os.listdir(path_img)):
                #lista de archivos
                files = os.listdir(path_img)
                print( "Archivos en carpeta media: " + ",".join(files))

                #remover archivos basura de osx
                try:
                    files.remove('.DS_Store')
                except ValueError:
                    pass

                #lista de archivos

                filenames = ','.join(files)

                #rutas completas a los archivos
                filepaths = [path_img + file for file in files]

                #se crea la nueva fila, con rutas
                new_row = [id, path, filenames]
                print(new_row)
                #se escribe la nueva fila en la tabla de salida
                found_reportwriter.writerow(new_row)
                count = count + 1

                #dirname = os.path.basename(path)
                #print("basename: " + os.path.basename(path))
                #os.rename(path, new_path)

            # si no existe carpeta de archivos media
            # se guarda una nueva entrada en el reporte sin media
            else:
                nomedia_row = [id, path, document_contents]
                nomedia_reportwriter.writerow(nomedia_row)
                print("No se encontro imagen media: " + path)

        #si no existe la(s) ruta(s)
        else:
            #Entrada en la tabla de faltantes
            missing_report_row = [id, path]
            missing_reportwriter.writerow(missing_report_row)

#Se imprime la cantidad de encontradas
print("encontradas: " + str(count))
