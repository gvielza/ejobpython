import pickle

class Vehiculo:
    nombre=""
    ruedas=0

    def __init__(self,nombre,ruedas):
        self.nombre=nombre
        self.ruedas=ruedas


v1=Vehiculo("BMW",4)
#exportar el vehiculo creado a fichero mediante pickle
fichero=open("vehiculo.txt",'wb')
pickle.dump(v1,fichero)
fichero.close()

#importar el fichero creado
fi=open('vehiculo.txt','rb')
vechicuo=pickle.load(fi)
print(vechicuo.nombre)
fi.close()

