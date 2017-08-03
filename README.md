# Wivo Technical Examination #
*Monday, 31th July, 2017*  
*Produced by Paolo Caviedes Saavedra*

## Requerimiento ##

Se adjuntan tres fuentes de datos distintas: events (csv), objects (xml) y metrics (json) . Se deben realizar las siguientes tareas:  
* Normalizar estas tres fuentes de datos en una base de datos SQL (se puede escoger mysql, postgresql o sqlite) y adjuntar el esquema de base de datos final.  
* Escribir un programa en el lenguaje de su preferencia que lea estas fuentes de datos entregadas en un único directorio, transforme los datos al esquema relacional y escriba en la base de datos SQL.  
* El mismo programa debe procesar otros archivos similares en el mismo directorio cuantas veces se requiera, pero solo debe procesar archivos nuevos o que hayan sido modificados en contenido. Los archivos siempre tendrán el mismo formato, pero el nombre podrá variar, ejemplo: events-20170731.csv, 123456789-metrics.json, etc.

## Descomposición del Problema ##

Para comenzar, se realiza el análisis de lo solicitado y la fuente de datos de cada uno de los archivos para determinar su relación. 

En términos de lo solicitado, se identifican los siguientes 3 elementos principales:  
* Se debe escribir un programa que realice la lectura de los archivos entregados en el directorio.  
* Estos archivos deben ser leídos y preparados para la inserción en una Base de Datos.  
* El modelo de Base de Datos a utilizar debe ser normalizado para la información a recibir.  

Observaciones importantes:  
* El programa debe realizar la lectura del directorio cada vez que se ejecute, sin embargo, los archivos a leer serán los que han sido modificados o los nuevos. 
* Los archivos a leer pueden tener distintos nombres, sin embargo, estos no se modifican en formato y siguen el mismo patrón ejemplo: events-20170731.csv, 123456789-metrics.json

## Desarrollo del Problema ##

En primer lugar, se realiza el análisis de los datos de fuente entregados. Para determinar el modelo de datos correspondiente, en este caso se crearon las tablas de acuerdo a la foto entregada en los archivos de este directorio. 

Posteriormente realicé la separación en módulos para la mejor comprensión del problema en este caso el script principal es main.py, las operaciones a la base de datos se realizan en sql_operations.py, los parsers a los archivos están en parsers.py y algunas utilidades en utils.py

Para resolver el requerimiento del análisis de archivos por nombre, utilicé la librería re con expresiones regulares, además creé una tabla en la BD para gestionar el histórico de los archivos ya leídos, los cuales se agregan una vez volcado a la BD. 
Luego para volcar la información a la BD se realiza la validación de cada registro sobre la misma, para evitar que al modificar un archivo, los registros que ya pertenecen a la BD sean agregados. Esta opción para el archivo event.csv se encuentra deshabilitada (comentada) para evitar largos tiempos de lectura a la BD, la puedes descomentar para verificar su funcionamiento, esto es en parsers.py line 99.

Por otro lado, obvie las claves foráneas para agilizar el proceso de volcado, sin embargo estas se pueden reconocer entre las tablas:

object(name) y events(object_name)  
Events(metric_name) y metric(name)  
metric(derived_from) y function(name)  

Para finalizar, cabe mencionar que las functions podrían ser agregadas a la base de datos como stored procedures, sin embargo, no lo hice para priorizar el proceso de volcado de información.
