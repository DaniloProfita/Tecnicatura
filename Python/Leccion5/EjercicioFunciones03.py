#Ejercicio 3: Funciones recursiva
#Imprimir numeros de 5 a 1 de manera descendiente usando funciones recursivas puede ser cualquier valor positivo, por ejemplo si pasamos el valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
#En caso de ser el numero 3 debe imprimir
# 3
# 2
# 1
#Si se ingresan numero negativos no imprime nada
def factorial(numero):
    if numero >= 1:
        print(numero)
        factorial(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto')
factorial(5)