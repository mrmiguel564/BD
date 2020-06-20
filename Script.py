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
	mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(20) Primary KEY, nombre VARCHAR(30), estado_civil VARCHAR(30), fecha_nacimiento VARCHAR(30), telefono VARCHAR(30), correo VARCHAR(30), genero VARCHAR(30), enfermedades_cronicas VARCHAR(30))")
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
tableName="Trabajador"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(20) Primary KEY, dia_de_paga VARCHAR(10), sueldo INT)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Surcursal"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (nombre_surcursal  VARCHAR(30) Primary KEY, telefono VARCHAR(30), ubicacion VARCHAR(30))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Beneficiario"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(50) Primary KEY, rut_asegurado VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Asegurado"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(50) Primary KEY, rut_asegurado VARCHAR(50), oficio VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Correo"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (rut  VARCHAR(50) Primary KEY, correo VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, rut_beneficiario VARCHAR(30), rut_asegurado VARCHAR(30), fecha_de_pago VARCHAR(30), monto de pago INT, fecha_vencimiento VARCHAR(30), fecha_contratacion VARCHAR(30), vigencia BOOL)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Cobros"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE"+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, numero_de_cobro INT, estado_cuota BOOL, precio_a_pagar INT, fecha_de_cobro VARCHAR(15))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
