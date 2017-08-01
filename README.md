# Wivo Technical Examination #
*Monday, 31th July, 2017*
*Produced by Paolo Caviedes Saavedra*

## Requerimiento ##

Se adjuntan tres fuentes de datos distintas: events (csv), objects (xml) y metrics (json) . Se deben realizar las siguientes tareas:  
* Normalizar estas tres fuentes de datos en una base de datos SQL (se puede escoger mysql, postgresql o sqlite) y adjuntar el esquema de base de datos final.  
* Escribir un programa en el lenguaje de su preferencia que lea estas fuentes de datos entregadas en un único directorio, transforme los datos al esquema relacional y escriba en la base de datos SQL.  
* El mismo programa debe procesar otros archivos similares en el mismo directorio cuantas veces se requiera, pero solo debe procesar archivos nuevos o que hayan sido modificados en contenido. Los archivos siempre tendrán el mismo formato, pero el nombre podrá variar, ejemplo: events-20170731.csv, 123456789-metrics.json, etc.

## Descomposición del Problema ##

Para comenzar el problema, en primer lugar se realiza el análisis de lo solicitado y la fuente de datos de cada uno de los archivos para determinar su relación. 

En terminos de lo solicitado, la descomposición del problema se muestra como sigue:  
* Se debe escribir un programa que realice la lectura de los archivos entregados en el directorio.  
* Estos archivos deben ser leidos y preparados para la inserción en una Base de Datos.  
* El modelo de Base de Datos a utilizar debe ser normalizado para la información a recibir.  

Observaciones importantes:  
* El programa debe realizar la lectura de los archivos cada vez que se ejecute, sin embargo, los archivos a leer serán los que han sido modificados o los archivos nuevos. 
* Los archivos a leer pueden tener distintos nombres, sin embargo estos no se modifican en formato y siguen el mismo patrón ejemplo: events-20170731.csv, 123456789-metrics.json

## Desarrollo del Problema ##

En primer lugar se realiza el analisis de los datos de fuente entregados. 

El primer archivo analizado es Objects.xml  

*** Objects.xml ***

:::xml
<row>
	  <id>1954</id>
	  <name>491245 - 212 SEXY EDP 30ML 2202005371</name>
	  <type>products</type>
	  <external_reference>491245 - 212 SEXY EDP 30ML 2202005371</external_reference>
	  <metadata>{}</metadata>
</row>