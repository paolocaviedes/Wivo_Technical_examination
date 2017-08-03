import os
from datetime import datetime
import mysql.connector
import re
from bs4 import BeautifulSoup
from sql_operations import object_verificator as verify_object, add_object, add_file,event_verificator as verify_event, add_event,function_verificator as verify_function, add_function, metric_verificator as verify_metric, add_metric
import json

clear = lambda: os.system('cls')

def files_parser(files,cursor,cnx):
	for file in files: 
		
			
		if file["extension"]==".json":
			#json parser
			clear()
			print "Analizando ",file["filename"],file["extension"],"..."
			jsonparser(file,cursor,cnx)
		
		elif file["extension"]==".xml":
			#xml parser
			# continue
			clear()
			print "Analizando ",file["filename"],file["extension"],"..."
			xmlparser(file,cursor,cnx)

		elif file["extension"]==".csv":
			# continue
			#csv parser
			clear()
			print "Analizando ",file["filename"],file["extension"],"..."
			csvparser(file,cursor,cnx)
		
		else: 
			print "Error - Archivo desconocido"

def xmlparser(file,cursor,cnx):
	infile = open(file["filename"]+file["extension"],"r")
	contents = infile.read()
	soup = BeautifulSoup(contents,'xml')

	objects_identifiers = soup.find_all('id')
	objects_names = soup.find_all('name')
	objects_type = soup.find_all('type')
	objects_external_reference = soup.find_all('external_reference')
	objects_metadata = soup.find_all('metadata')

	for i in range(0, len(objects_identifiers)):
		object_identifier= objects_identifiers[i].get_text()
		object_name= objects_names[i].get_text()
		object_type= objects_type[i].get_text()
		object_external_reference =  objects_external_reference[i].get_text()
		object_metadata = objects_metadata[i].get_text()
		registry = {"object_identifier":object_identifier, "object_name":object_name, "object_type":object_type, "object_external_reference":object_external_reference, "object_metadata":object_metadata}
		if verify_object(registry,cursor,cnx):
			# print registry
			add_object(registry,cursor,cnx)
			
		else: 
			print "Info - Objeto ya existente en BD ",object_identifier," - ",object_name
	add_file(file,cursor,cnx)
	print "Info - Archivo actualizado en BD"

def csvparser(file,cursor,cnx):

	cadena_inicial=file["filename"]+file["extension"]+" |" + "".ljust(25,"-") + "|"+ " 0 %"
	cadena=file["filename"]+file["extension"]+" |" + "".ljust(25,"-") + "|"+ " 0 %"
	porcentaje_inicial=0
	porcentaje=0
	# print cadena_inicial

	archivo=open(file["filename"]+file["extension"])
	lineas = len(archivo.readlines())
	archivo.close

	archivo= open(file["filename"]+file["extension"],"r")
	counter=0
	for linea in archivo:
		if counter!=0:
			counter+=1
			avance = int(((float(counter) / float(lineas))*100)/4)*"|"
			porcentaje= round(((float(counter) / float(lineas))*100),2)
			
			cadena = file["filename"]+file["extension"]+" |" + avance.ljust(25,"-") + "| "+str(porcentaje)+" %"
			
			lista=linea.strip().split(",")
			if len(lista)==4:
				object_name=lista[0]
				event=lista[1]
				value=lista[2]
				metric_name=lista[3]
			elif len(lista)==5:
				object_name=lista[0]+lista[1]
				event=lista[2]
				value=lista[3]
				metric_name=lista[4]
				
			#Descomentar e indentar para realizar la comprobacion de registros repetidos. 	
			# if verify_event({"object_name":object_name,"event":event,"value":value,"metric_name":metric_name},cursor,cnx):
			add_event({"object_name":object_name,"event":event,"value":value,"metric_name":metric_name},cursor,cnx)
			# else: 
				# print "Info - El evento ",event, " ya existe en la BD"

		
		elif counter==0:
			counter+=1

		# print str(counter) ,"/", str(lineas) ,porcentaje," %"
		# porcentaje_inicial=porcentaje
		if cadena!=cadena_inicial:
			clear()
			print "Analizando ",file["filename"],file["extension"],"..."
			print cadena
			cadena_inicial=cadena


		
	add_file(file,cursor,cnx)

	archivo.close()

def jsonparser(file,cursor,cnx):
	archivo=open(file["filename"]+file["extension"],"r")

	for linea in archivo:
		
		linea=linea.strip()
		structure=json.loads(linea)
		print structure

		name = structure["name"]
		unit = structure["unit"]
		representation = structure["representation"]
		derived_from = structure["derived_from"]

		if derived_from!=None:
			parameters=derived_from["parameters"]
			#agregar function
			if verify_function({"name":name,"parameters":parameters},cursor,cnx):
				add_function({"name":name,"parameters":parameters},cursor,cnx)
				

		#agregar metric
		if verify_metric({"name":name,"unit":unit,"representation":representation,"derived_from":derived_from},cursor,cnx):
			add_metric({"name":name,"unit":unit,"representation":representation,"derived_from":derived_from},cursor,cnx)
	add_file(file,cursor,cnx)
	archivo.close()

