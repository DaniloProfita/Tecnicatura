#Ejercicio 2: Modificar los elementos de una lista 
#Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista
#multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
num = int(input("Ingrese un numero para multiplicar la lista: "))

for indice, i in enumerate(lista):
    lista[indice] *= num

print(f'La lista multiplicada por {num} es: {lista}')