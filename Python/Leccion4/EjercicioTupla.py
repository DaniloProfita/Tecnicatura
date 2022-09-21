import math #Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
'''
tupla = (13, 1, 8, 3, 2, 5, 8)
Crear una lista que solo incluya los numeros menores a 5
e imprimir por consola [1, 3, 2]
'''
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for tuplita in tupla:
    if tuplita < 5:
        lista.append(tuplita)

print(lista)


#Ejercicio de matematicas
#Para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo'))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo'))
print(f'\n Si raiz cuadrada es: {math.sqrt(numero):.2f} ')