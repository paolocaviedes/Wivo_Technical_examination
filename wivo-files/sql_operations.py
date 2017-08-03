import os
from datetime import datetime
import mysql.connector
import re
from bs4 import BeautifulSoup
import json

def execute_query(query):
	cursor.execute(query)
	response = cursor.fetchall()
	return response

def open_conx():
	try:
		cnx = mysql.connector.connect(user='root', password='561g9643',host='127.0.0.1',database='wivo')
		cursor = cnx.cursor(buffered=True)
		return cnx,cursor
	except :
		print "Couldnt connect to BD, check connection information and MySQL service"
	

def close_cnx(cnx,cursor):
	cnx.commit()
	cursor.close()
	cnx.close()

def add_file(dictionary,cursor,cnx):
	"""
	Funcion que inserta un Archivo en la tabla file_registry, 
	recibe un diccionario con la informacion a agregar.
	"""
	query = ("INSERT INTO file_registry"
               "(name,extension,created,edited,directorio) "
               "VALUES (%s, %s, %s, %s, %s)")
	data_query = (dictionary['filename'], dictionary['extension'], dictionary['created'], dictionary['edited'], dictionary['path'])
	cursor.execute(query,data_query)
	# cnx.commit()
	# response = cursor.fetchall()
	# return response

def find_file(dictionary,cursor,cnx):
	"""
	Fucion que recibe un diccionario con un archivo a buscar y 
	retorna False en caso de que no exista y retorna el registro en caso de encontrarlo.
	"""
	query = ("SELECT * FROM file_registry where name = %s and extension = %s ORDER BY id DESC LIMIT 1")
	data_query= (dictionary["filename"],dictionary["extension"])
	cursor.execute(query,data_query)
	# cnx.commit()
	response = cursor.fetchall()
	if len(response) == 0: 
		return False
	else:
		return response


def object_verificator(registry,cursor,cnx):
	"""
	Esta funcion se encarga de verificar que el objeto a agregar no exista en la BD,
	recibe el diccionario con la informacion del archivo y 
	retorna True o False dependiendo si existe o no el registro.
	"""
	query = ("SELECT * FROM object where id = %s and name = %s and type = %s and external_reference = %s and metadata = %s")
	data_query= (registry["object_identifier"],registry["object_name"],registry["object_type"],registry["object_external_reference"],registry["object_metadata"],)
	try:
		cursor.execute(query,data_query)
		cnx.commit()
		response = cursor.fetchall()
		# print "Info - Consulta de busqueda de objeto ok"

		if len(response) == 0: 
			return True
		else:
			return False
		
	except:
		return "Error - Error en Consulta de objeto"
		
	finally:
		return "Error Desconocido"

def add_object(object_to_add, cursor,cnx):
	"""
	Funcion que se encarga de agregar un objeto en Objects. 
	Recibe un diccionario con el objeto a agregar.
	"""
	query = ("INSERT INTO object"
               "(id,name,type,external_reference,metadata) "
               "VALUES (%s, %s, %s, %s, %s)")
	data_query = (object_to_add['object_identifier'],object_to_add['object_name'],object_to_add['object_type'],object_to_add['object_external_reference'],object_to_add['object_metadata'] )
	try:
		cursor.execute(query,data_query)
		print "Info - El Objeto: ", object_to_add['object_identifier'], "fue agregado con exito"
	except :
	 	print "Error - Objeto no agregado, error desconocido"
	
def event_verificator(registry, cursor,cnx):
	"""
	Esta funcion se encarga de verificar que el objeto a agregar no exista en la BD,
	recibe el diccionario con la informacion del archivo y 
	retorna True o False dependiendo si existe o no el registro.
	"""
	query = ("SELECT * FROM events where object_name = %s and event = %s and value = %s and metric_name = %s")
	data_query= (registry["object_name"],registry["event"],registry["value"],registry["metric_name"])
	try:
		cursor.execute(query,data_query)
		response = cursor.fetchall()
		# print "Info - Consulta de busqueda de evento ok"

		if len(response) == 0: 
				return True
		else:
				return False
		
	except:
		return "Error - Error en Consulta de event"


def add_event(event_to_add, cursor,cnx):
	"""
	Funcion que se encarga de agregar un evento en event. 
	Recibe un diccionario con el event a agregar.
	"""
	query = ("INSERT INTO wivo.events"
               "(object_name,event,value,metric_name) "
               "VALUES (%s, %s, %s, %s)")
	data_query = (event_to_add['object_name'], event_to_add['event'], event_to_add['value'], event_to_add['metric_name'] )
	# print data_query
	try:
		cursor.execute(query,data_query)
		cnx.commit()
		# print "Info - El Evento: ", event_to_add['object_name'], "fue agregado con exito"
	except :
		print "Error - Evento no agregado, error desconocido"

def metric_verificator(registry, cursor, cnx):
	"""
	Funcion que se encarga de verificar si existe la metrica en la BD, recibe el registro a evaluar
	"""
	query = ("SELECT * FROM metric where name = %s and unit = %s and representation = %s and derived_from = %s")
	data_query= (registry["name"],registry["unit"],registry["representation"],registry["derived_from"],)
	try:
		cursor.execute(query,data_query)
		response = cursor.fetchall()
		# print "Info - Consulta de busqueda de evento ok"

		if len(response) == 0: 
				return True
		else:
				return False
		
	except:
		return "Error - Error en Consulta de event"

def add_metric(metric_to_add, cursor, cnx):
	"""
	Funcion que se encarga de agregar una metrica en metric. 
	Recibe un diccionario con la metrica a agregar.
	"""

	query = ("INSERT INTO wivo.metric"
               "(name,unit,representation,derived_from) "
               "VALUES (%s, %s, %s, %s)")
	if metric_to_add['derived_from']==None:
		data_query = (metric_to_add['name'], metric_to_add['unit'], metric_to_add['representation'], metric_to_add['derived_from'] )
		
	else:
		data_query = (metric_to_add['name'], metric_to_add['unit'], metric_to_add['representation'], metric_to_add['derived_from']["function"] )
	# print data_query
	try:
		cursor.execute(query,data_query)
		cnx.commit()
		# print "Info - El metriceo: ", event_to_add['object_name'], "fue agregado con exito"
	except :
		print "Error - Metrica no agregada, error desconocido"

def function_verificator(registry, cursor, cnx):
	"""
	Funcion que se encarga de verificar si existe la function en la BD, recibe el registro a evaluar
	"""
	query = ("SELECT * FROM function where name = %s and parameters = %s")
	data_query= (registry["name"],registry["parameters"])
	try:
		cursor.execute(query,data_query)
		response = cursor.fetchall()
		# print "Info - Consulta de busqueda de evento ok"

		if len(response) == 0: 
				return True
		else:
				return False
		
	except:
		return "Error - Error en Consulta de event"

def add_function(function_to_add, cursor, cnx):
	"""
	Funcion que se encarga de agregar una function en function. 
	Recibe un diccionario con la funcion a agregar.
	"""
	print "-------"
	print function_to_add
	query = ("INSERT INTO wivo.function"
               "(name,parameters) "
               "VALUES (%s, %s)")
	data_query = (function_to_add['name'], str(function_to_add['parameters'][0]) )
	try:
		cursor.execute(query,data_query)
		# print "Info - El metriceo: ", event_to_add['object_name'], "fue agregado con exito"
	except :
		print "Error - Function no agregada, error desconocido"

