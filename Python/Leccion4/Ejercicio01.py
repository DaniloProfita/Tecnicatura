#Ejercicio 1: Llenar una lista
#Llenar una lista con los numero del 1 al 50, luego mostrar
#La lista con el bucle for, los elementos deben mostrarse de las siguiente forma:
#1 - 2 - 3 - 4 - 5 - ... - 50

lista = []

for i in range(1, 51):
    lista.append(i)
for i in range(1, 51):
    print(i, end=' - ')
