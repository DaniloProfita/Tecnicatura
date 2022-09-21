#Ejercicio 2: Operaciones de conjuntos con listas
#Escriba un programa que tenga 2 listas que a continuacion...
#Cree las siguientes listas (en las que no deben haber repeticion)


lista1 = ['Juventus', 'Roma', 'Torino', 'Udinese', 'Sampdoria', 'Milan', 'Inter']
lista2 = ['Milan', 'Inter', 'Empoli', 'Atalanta', 'Napoli', 'Juventus', 'Roma']
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# 1 Lista de palabras que aparecen en las listas
print(conjunto1 | conjunto2)

# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
print(conjunto1 - conjunto2)

# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
print(conjunto2 - conjunto1)

# 4 Lista de palabras que aparecen en ambas listas
print(conjunto1 & conjunto2)