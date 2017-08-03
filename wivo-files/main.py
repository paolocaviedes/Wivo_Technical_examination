import os
from datetime import datetime
import mysql.connector
import re
from bs4 import BeautifulSoup
from sql_operations import open_conx as connect, close_cnx as disconnect, execute_query
from utils import read_path as obtain_files
from parsers import files_parser

cnx,cursor = connect()
files= obtain_files(cursor,cnx)
files_parser(files,cursor,cnx)
 
print "Operacion realizada con exito"
raw_input("Presione una tecla para finalizar.")

disconnect(cnx,cursor)