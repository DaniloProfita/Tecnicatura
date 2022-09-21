#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillo
#Nombre: Aragon                     #Nombre: Gandalf            #Nombre: Legolas
#Clase: Guerrero                    #Clase: Mago                #Clase: Arquero
#Raza: Dúnadan del norte            #Raza: Istar                #Raza: Elfo Sindar

personajes = []
P1 = {
    'Nombre': 'Aragon',
    'Clase': 'Guerrero',
    'Raza': 'Dúnadan del norte',
}
P2 = {
    'Nombre': 'Gandalf',
    'Clase': 'Mago',
    'Raza': 'Istar',
}
P3 = {
    'Nombre': 'Legolas',
    'Clase': 'Arquero',
    'Raza': 'Elfo Sindar',
}
personajes.append(P1)
personajes.append(P2)
personajes.append(P3)
print(personajes)
