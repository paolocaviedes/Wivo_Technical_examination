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

***Objects.xml***

```xml
<row>
	  <id>1954</id>
	  <name>491245 - 212 SEXY EDP 30ML 2202005371</name>
	  <type>products</type>
	  <external_reference>491245 - 212 SEXY EDP 30ML 2202005371</external_reference>
	  <metadata>{}</metadata>
</row>
```

Como se puede observar en la estructura xml anteriormente descrita, la información relevante a almacenar se estructura de la siguiente manera. 

|   Object   | datatypes  |
| ---------- | ---------- |
| id_object  | integer   |
| name   | varchar(45)   |
| type   | varchar(45)   |
| external_reference   | varchar(45)   |
| metadata | varchar(45)   |

Para determinar los largos adecuados para los campos, fue necesario programar un script que realice al calculo de los objetos con mayor largo, el cual se encuentra en xml_determine_len.py; Los resultados obtenidos fueron:
~~~
La logitud maxima del campo id es:  5
La logitud maxima del campo name es:  44
La logitud maxima del campo type es:  11
La logitud maxima del campo external reference es:  44
La logitud maxima del campo metadata es:  2
~~~

Luego esta tabla es creada en la Base de Datos.
```sql
'objects', CREATE TABLE 'objects' (
  'id' int(11) NOT NULL,
  'name' varchar(45) NOT NULL,
  'type' varchar(45) NOT NULL,
  'external_reference' varchar(45) NOT NULL,
  ' metadata' varchar(150) NOT NULL,
  PRIMARY KEY ('id')
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

