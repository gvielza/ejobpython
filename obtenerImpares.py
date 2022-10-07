#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una
# lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce
entrada=input("entre los numeros que desee analizar separados por coma: ")
cadena=entrada.split(',')
numeros=[int(a) for a in cadena]

def impares(x):
    if(x%2!=0):
        return True
    else:
        return False

impares = list(filter(impares, numeros))

#con lambda sería impares = list(filter(lambda x:(x % 2 != 0), numeros))

suma=reduce((lambda x,y:x+y),impares)


print("Los numeros impares son: ", impares, " y la suma de ellos es: ", suma)