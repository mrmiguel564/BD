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
	mycursor.execute("create database "+NombreBD+";")
	mycursor.execute("use "+NombreBD)
	print("BD "+NombreBD+" Creada")
except:
	mydb.close()
	mydb = mysql.connector.connect(host=Ip,user=User,password=Passwd,database=NombreBD)
	mycursor = mydb.cursor()
	print("BD "+NombreBD+" ya estaba Creada")

#---------------------------------------------
tableName="Persona" 		

try:										 	#columnas para modificar mysql lenguaje https://www.w3schools.com/python/python_mysql_create_table.asp
	mycursor.execute("CREATE TABLE " +tableName+" (rut  VARCHAR(20) Primary KEY, nombre VARCHAR(30), estado_civil VARCHAR(30), fecha_nacimiento VARCHAR(30), genero VARCHAR(30)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Cliente"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (rut  VARCHAR(50) Primary KEY, fondo_de_salud VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Trabajador"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (rut  VARCHAR(20) Primary KEY, dia_de_paga VARCHAR(10), sueldo INT)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Surcursal"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (nombre_surcursal VARCHAR(30) Primary KEY, telefono VARCHAR(30), ubicacion VARCHAR(30))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Beneficiario"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (rut  VARCHAR(50) Primary KEY, rut_asegurado VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Asegurado"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (rut  VARCHAR(50) Primary KEY, rut_asegurado VARCHAR(50), oficio VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Correo"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (rut  VARCHAR(50) Primary KEY, correo VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, rut_beneficiario VARCHAR(30), rut_asegurado VARCHAR(30), fecha_de_pago VARCHAR(30), monto de pago INT, fecha_vencimiento VARCHAR(30), fecha_contratacion VARCHAR(30), vigencia BOOL)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Cobros"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, numero_de_cobro INT, estado_cuota BOOL, precio_a_pagar INT, fecha_de_cobro VARCHAR(15))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza_de_Muerte"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, causas_de_muerte_validas VARCHAR(50))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza_de_Vida_Entera"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, edad_maxima_permanencia INT)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza_de_seguro_de_vida_flexible"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, monto_retiro_parcial INT, minimo_años_permanencia INT, numero_retiros_parciales_anuales INT)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza_de_seguro_de_supervivencia"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, edad_minima_para_cobrar INT)")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------
tableName="Poliza_de_seguro_de_invalidez"

try:                                             #columnas para modificar mysql lenguaje
    mycursor.execute("CREATE TABLE "+tableName+" (numero_de_poliza  VARCHAR(10) Primary KEY, enfermedades VARCHAR(30), accidentes_naturales VARCHAR(30), accidentes_laborales VARCHAR(30), accidentes_ambientales VARCHAR(30))")
except:
    print("tabla "+tableName+" ya estaba Creada")
else:
    print("tabla "+tableName+" Creada")
#---------------------------------------------

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)

sql = "INSERT INTO Persona (rut, nombre, estado_civil, fecha_nacimiento, genero) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Peter', 'Lowstreet 4', 'Lowstreet 4', 'Lowstreet 4', 'Lowstreet 4'),
  ('Amy', 'Apple st 652', 'Apple st 652', 'Apple st 652', 'Apple st 652'),
  ('Hannah', 'Mountain 21', 'Mountain 21', 'Mountain 21', 'Mountain 21'),
  ('Michael', 'Valley 345', 'Valley 345', 'Valley 345', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2', 'Ocean blvd 2', 'Ocean blvd 2', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1', 'Green Grass 1', 'Green Grass 1', 'Green Grass 1'),
  ('Richard', 'Sky st 331', 'Sky st 331', 'Sky st 331', 'Sky st 331'),
  ('Susan', 'One way 98', 'One way 98', 'One way 98', 'One way 98'),
  ('Vicky', 'Yellow Garden 2', 'Yellow Garden 2', 'Yellow Garden 2', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38', 'Park Lane 38', 'Park Lane 38', 'Park Lane 38'),
  ('William', 'Central st 954', 'Central st 954', 'Central st 954', 'Central st 954'),
  ('Chuck', 'Main Road 989', 'Main Road 989', 'Main Road 989', 'Main Road 989'),
  ('Viola', 'Sideway 1633', 'Sideway 1633', 'Sideway 1633', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()