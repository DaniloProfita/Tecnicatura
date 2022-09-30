# Ejercicio 2: Funcion con * args para multiplicar 
# Crea una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumento

def multiplicar(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado
print(multiplicar(3, 5, 10))