import _sqlite3
conn = _sqlite3.connect('miaplicacion.db')
cursor=conn.cursor()

def verificar(username,password)

rows=cursor.execute("SELECT * FROM users WHERE username='gvielza'")
for row in rows:
    print(row)


cursor.close()
conn.close()