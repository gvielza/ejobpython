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
