#Ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos.
#Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono, el programa tenfra el siguiente menu:
#1. Nuevo contacto
#2. Borrar contacto
#3. Ver contactos existentes
#4. Salir

agenda = {}
while True:
    print('\t MENU ')
    print('\n 1. Nuevo contacto')
    print('\n 2. Borrar contacto')
    print('\n 3. Ver contactos existentes')
    print('\n 4. Salir')
    opcion = int(input("\n Digite una opcion del menu: "))
    print()
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('\n Contacto agregado correctamente')
        else:
            print('\n Contacto existente')
    elif opcion == 2:
        nombre = input("Digite el nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print('Se ha eliminado correctamente')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos: \n')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave} - Telefono: {valor} ')
    elif opcion == 4:
        print(f'\n Gracias por utilizar su agenda de contactos')
        break
    else:
        print(f'\n Error, opcion en el menu no existene')
        print()