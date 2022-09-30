class Vehiculo:
    Color="Azul"
    Ruedas=4
    Puertas=4

class Coche(Vehiculo):
    velocidad=150
    cilindrada="1.4L"

c=Coche
c.Color="Verde"
print("El color del coche ahora es ",c.Color)

class Alumno:

    def __int__(self):
        self.nombre=input("ingrese su nombre: ")
        self.nota=int(input("Ingrese su nota: "))

    def isAprobado(self):
        if(self.nota<60):
            print(self.nombre, "estás reprobado☺ Ups!")
        else:
            print(self.nombre,"bieeen, aprobaste☻")

alumno=Alumno()
alumno.__int__()
alumno.isAprobado()

