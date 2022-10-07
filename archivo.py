import operaciones as oper

numero1=input("escriba el primer numero: ")
numero2=input("Escriba el segundo numero: ")

operacion=input("Escoga el número segun la operacion que desee""\n"
                "1-Suma" "\n"
                "2-Resta" "\n"
                "3-multiplicar""\n"
                "4-dividir" "\n")

if(int(operacion)==1):
    print("La suma de los numeros entrados es",oper.sumar(int(numero1),int(numero2)))

if (int(operacion) == 2):
    print("La resta de los numeros entrados es", oper.restar(int(numero1), int(numero2)))

if(int(operacion)==3):
    print("La multiplicacion de los numeros entrados es",oper.multiplicar(int(numero1),int(numero2)))

if(int(operacion)==4):
    print("La division de los numeros entrados  es",oper.dividir(int(numero1),int(numero2)))