#Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

entradas=input("Ingrese una lista de paises separados por coma: ")



paises=entradas.split(',')
print(paises)

print("Los países ordenados y sin repetir serían: ",sorted(set(paises)))