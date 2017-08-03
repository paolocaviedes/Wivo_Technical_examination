import os
from datetime import datetime
import mysql.connector
import re
from bs4 import BeautifulSoup
from sql_operations import find_file

def isvalid_filename(filename):
	valid_name_json = re.compile('([\d]+-)*metrics(\.json)') # Expresion regular para 123456789-metrics.json y metrics.json
	valid_name_csv = re.compile('events(-[\d]+)*(\.csv)') # Expresion regular para events-20170731.csv y events.csv

	json_valid = valid_name_json.match(filename)
	csv_valid = valid_name_csv.match(filename)

	valid_name_xml = "objects.xml"

	if valid_name_xml == filename:
		xml_valid = True
	else: xml_valid = False

	if json_valid or csv_valid or xml_valid:
		return True
	else: return False

def ismodified_filename(dictionary, cursor, cnx):
	"""
	
	"""
	#Se revisa si el archivo existe en la BD
	response= find_file(dictionary,cursor,cnx)
	#Si no existe se debe revisar
	if not response:
		return True

	#Si existe se revisa la fecha de edicion
	else:
		#Si fue editado se debe revisar
		identifier_bd, name_bd, extension_bd, created_bd, edited_bd, directorio_bd = response[0]

		if dictionary["edited"] != str(edited_bd):
			return True
		#Si no fue editado no se hace nada
		else: return False

def read_path(cursor,cnx):
	ruta_app = os.getcwd()  # obtiene ruta del script 
	contenido = os.listdir(ruta_app) # obtiene lista con archivos/dir
	formato = '20%y-%m-%d %H:%M:%S'

	files=[]
	for file in contenido:
		archivo = ruta_app + os.sep + file
		filename, file_extension = os.path.splitext(file)
		estado = os.stat(file)
		modificado = datetime.fromtimestamp(estado.st_mtime) #fecha de modificacion
		modificado = modificado.strftime(formato) # formato aplicado

		creado = datetime.fromtimestamp(estado.st_ctime) #fecha de modificacion
		creado = creado.strftime(formato) # formato aplicado
		if isvalid_filename(filename+file_extension):
			if ismodified_filename({"filename":filename,"extension":file_extension,"created":creado,"edited":modificado,"path":archivo},cursor,cnx):
				files.append({"filename":filename,"extension":file_extension,"created":creado,"edited":modificado,"path":archivo})

	return files

