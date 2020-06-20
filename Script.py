import mysql.connector

#modificar esto segun tus datos
Passwd="M564231897"
Ip="localhost"
User="root"

mydb = mysql.connector.connect(host=Ip,user=User,password=Passwd)
mycursor = mydb.cursor()

#---------------------------------------------
NombreBD="seguros_vida"
try:
	mycursor.execute("CREATE DATABASE "+NombreBD+"; use "+NombreBD)
except:
	mydb = mysql.connector.connect(host=Ip,user=User,password=Passwd,database=NombreBD)
	mycursor = mydb.cursor()
	print("BD "+NombreBD+" ya estaba Creada")
else:
	print("BD "+NombreBD+" Creada")
#---------------------------------------------
tableName="Persona" 		

try:										 	#columnas para modificar mysql lenguaje https://www.w3schools.com/python/python_mysql_create_table.asp
	mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(50) Primary KEY, name VARCHAR(50))")
except:
	print("tabla "+tableName+" ya estaba Creada")
else:
	print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Cliente"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(50) Primary KEY, fondo_de_salud VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
