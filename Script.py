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
tablas=(
	(('persona',		)	,"rut  VARCHAR(20) PRIMARY KEY, nombre VARCHAR(30), estado_civil VARCHAR(30) , fecha_nacimiento VARCHAR(30) , genero VARCHAR(30))"),
	(('cliente',		)	,""),
	(('trabajador',		)	,""),
	(('surcursal',		)	,""),
	(('asignacion',		)	,""),
	(('beneficiario',	)	,""),
	(('asegurado',		)	,""),
	(('correo',			)	,""),
	(('poliza',			)	,""),
	(('cobros',			)	,""),
	(('de_Muerte,',		)	,""),
	(('de_Vida_Entera',	)	,""),
	(('de_vida_flexible',)	,""),
	(('de_supervivencia',)	,""),
	(('de_invalidez',	)	,"")
	)
variables=[]
for x in range(len(tablas)):
	variables.append(True)

mycursor.execute("SHOW TABLES")
for x in mycursor:
	i=0
	for y in tablas:
		if x ==y[0]:
			variables[i]=False
		i=i+1
i=0

for y in variables:
	if(y):
		tableName=tablas[i][0]
		try:										 	
			mycursor.execute("CREATE TABLE "+tablas[i][0][0]+" ("+tablas[i][1]+")")
		except:
			print("ERROR tabla "+tablas[i][0][0]+" no se pudo Crear")
	i=i+1

"""
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
"""