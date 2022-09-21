#Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo numericos
#Utilizando argumentos variables *args como parametro de la funcion
#y agregar como resultado la suma de todos los valores pasados como argumentos

def suma(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(suma(3, 6, 9))