#leer fichero

f=open('../pruebafuera.txt','r')
datos=f.read()
print(datos)
f.close()

#escribir fichero


def escribe(fichero,datos):
    f=open(fichero,'w')
    for linea in datos:
        if(not linea.endswith('\n')):
            linea=linea+'\n'
            f.write(linea)
    f.close()

lista=[
    'una linea',
    'dos lineas\n',
    'tres lineas'
]
escribe('mifichero.txt',lista)
