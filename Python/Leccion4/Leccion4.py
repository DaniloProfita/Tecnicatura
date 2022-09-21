#lista = Ariel, Liliana, Natalia, Osvaldo

'''
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2])
print(nombres[ :3])
print(nombres[1: ])

#Modificar valores
nombres[2] = 'Liliana'
nombres[0] ='Natalia'
print(nombres)

#Iterar una lista
for nombre in nombres:#nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene el array
print(len(nombres))

#Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

#Incertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)


#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)


#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2]
print(nombres)

#Eliminar, borrar o limpiar los elementos
nombres.clear()
print(nombres)
'''

'''
#Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

#Mostrar de manera inversa
print(cocina[-1])


#Acceder a un rango
print(cocina[0:2])


#Recorremos los elementos de una tupla
for cocinar in cocina:
    print(cocinar, end=' ')

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n',cocina)

#del cocina para eliminar la tupla
'''
'''
#Tipo set
#No mantiene un indice, por cada ejecucion cambian de posicion
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))

#Revisa si un elemento existe dentro de set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra')
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')
print(planetas)
planetas.discard('Tierra')#Este no marca el error si no existe
print(planetas)

#Limpiar se
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
print(planetas)
'''
'''
#'Maradona': 10 Un diccionario esta compuesto por dos elementos
#Una llave y un valor
#dict(key, value)
diccionario = {
    'IDE': 'Integrated Developemnt Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
print(len(diccionario))
print(diccionario)

#Acceder a uin diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer los elemento
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():#Usamos una funcion para acceder al valor
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)#Devuelve un boolean

#Agrega un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
'''
'''
#Concatenar listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2 #Concatenacion
print(lista3)

lista3.extend([7, 8, 9, 1])#Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))#Funcion para ubicar en que indice esta ese valor ingresado, si no existe marca un error

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))

#Para poner la lista al reves
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo elementos
lista = [1, 2, 3] * 2
print(lista)

#Metodos de ordenamiento
lista3.sort()#Ordena de forma ascendente 
print(lista3)
lista3.sort(reverse=True)#Ordena de forma descendiente
print(lista3)

#Puede tener diferentes tipos de datos dentro
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

#Preguntamos si existe el numero 4 en la tupla
print(4 in tupla)#Devuelve un tipo boolean
#Lo que podemos usar dentro de tuplas son: index, count, len
#En tuplas se pueden convertir de tupla a lista y de lista a tupla
'''


'''
#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el numero 3 no esta en el conjunto 1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)#Devuelve booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2#La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2#Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2#Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)


conjunto3 = conjunto2 ^ conjunto1#Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto2 | conjunto1
print(conjunto2.issubset(conjunto3))#Preguntamos si un conjunto es subconjunto del otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))#Preguntamos si es un superconjunto del otro

#Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))#No hay cosas en comun

#Convertir un conjunto totalmente inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea totalmente inmutable
#No se puede agregar, modificar ni eliminar elementos del conjunto
'''
'''
#Repaso Diccionarios
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red', 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)
#Como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel' : {'Edad' : 40, 'Altura' : 1.83}, 'Osvaldo' : [45, 1.85], 'Natalia' : [35, 1.67]}
print(diccionario2)
'''
'''
seleccionArgentina = {
    10: {'Nombre':'Lionel Messi', 'Edad':35, 'Altura':1.70, 'Precio': '50M', 'Posicion':'Extremo Derecho'},
    11: {'Nombre':'Angel Di Maria', 'Edad':34, 'Altura':1.80, 'Precio': '12M', 'Posicion':'Extremo Derecho'},
    21: {'Nombre':'Paulo Dybala', 'Edad':28, 'Altura':1.77, 'Precio': '35M', 'Posicion':'Media Punta'},
    19: {'Nombre':'Nicolas Otamendi', 'Edad':34, 'Altura':1.83, 'Precio': '3.5M', 'Posicion':'Defensa Central'},
    1: {'Nombre':'Franco Armani', 'Edad':35, 'Altura':1.89, 'Precio': '3.5M', 'Posicion':'Portero'},
    20: {'Nombre':'Giovani Lo Celso', 'Edad':26, 'Altura':1.77, 'Precio':'22M', 'Posicion':'Mediocampista Cental'},
    8: {'Nombre':'Marcos Acuña', 'Edad':30, 'Altura':1.72, 'Precio':'15M', 'Posicion':'Lateral Izquierdo'},
    5: {'Nombre':'Leando Paredes', 'Edad':28, 'Altura':1.80, 'Precio':'17M', 'Posicion':'Mediocampista Central Defensivo'},
    22: {'Nombre':'Lautaro Martinez', 'Edad':25, 'Altura':1.74, 'Precio':'75M', 'Posicion':'Delantero Central'}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores:', end=' ')
print(len(seleccionArgentina))
'''
'''
#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final 
elementoBorrado =pila.pop()
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora queda asi: {pila}')


#Colas con listas
#Estructura de datos de tipo fifo(first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira} ')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira} ')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira} ')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira} ')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira} ')
print(cola)
'''

