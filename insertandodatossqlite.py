import _sqlite3
#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido
# que también será de tipo texto.Una vez creada la tabla, tenéis que insertarle datos,
# como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
opciones=input("Para agregar un nuevo alumno presione 1 o 2 para ver lo que ya están insertados: ")



def insertar_alumno(id,nombre,apellido):
    conn=_sqlite3.connect("alumnos.db")
    cursor=conn.cursor()
    query='''INSERT INTO alumnos(id,nombre,apellido) VALUES(?,?,?)'''
    rows=cursor.execute(query,(id,nombre,apellido))
    conn.commit()
    cursor.close()
    conn.close()
    print('El alumno con id: ',id,", nombre: ",nombre,"y apellido: ",apellido," fue insertado en la BD")
    mostrar()

def mostrar():
    conn = _sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    query = '''SELECT * FROM alumnos'''
    rows = cursor.execute(query)
    for row in rows:
        print(row)
    cursor.close()
    conn.close()



def insertar():
    id = input("Para Insertar un nuevo alumno escribe el identificador: ")
    nombre = input("Ahora el nombre: ")
    apellido = input("ahora el apellido: ")
    insertar_alumno(id, nombre, apellido)

if(int(opciones)==1):
    insertar()
else:
    mostrar()
