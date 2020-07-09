import mysql.connector
import json
#modificar esto segun tus datos
Passwd="M564231897"
Ip="localhost"
User="root"

mydb = mysql.connector.connect(host=Ip,user=User,password=Passwd)
mycursor = mydb.cursor()
#---------------------------------------------
NombreBD="seguros_vida"
try:
	mydb = mysql.connector.connect(host=Ip,user=User,password=Passwd,database=NombreBD)
	mycursor = mydb.cursor()
	print(" Conexion extablecida con: "+NombreBD)
except:
	print(" No se pudo establecer la conexion")
#---------------------------------------------

with open("C:/Users/mr_miguel/Documents/BD/datos.json") as file:
    data = json.load(file)



for y in data:
	print(y)
	try:
		mycursor.execute("insert into "+y )
	except:
		print("no se pudo insertar los datos")
	


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