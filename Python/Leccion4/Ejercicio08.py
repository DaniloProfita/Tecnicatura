#Ejercicio 8: Menu interactico - Cajero automatico
#Hacer un programa que simule un cajero automatico con un saldo inicial de $1.000 y tendra el siguiente menu de opciones
#1. Ingresar dinera en la cuenta
#2. Retirar dinero de la cuenta
#3. Mostrar dinero disponible
#4. Salir

saldo = 1000
while True:
    print('\t MENU ')
    print('\n 1. Ingresar dinero en la cuenta')
    print('\n 2. Retirar dinero de la cuenta')
    print('\n 3. Mostrar dinero disponible')
    print('\n 4. Salir')
    opcion = int(input("\n Digite una opcion del menu: "))
    print()
    if opcion == 1:
        ingresa = float(input('\n Cuanto dinero desea ingresar => '))
        saldo += ingresa
        print(f'\n Dinero en la cuenta: ${saldo} ')
    elif opcion == 2:
        retira = float(input('\n Cuanto dinero desea retirar => '))
        if retira > saldo:
            print('\n No tiene esa cantidad de dinero')
        else:
            saldo -= retira
            print(f'\n Dinero en la cuenta: ${saldo} ')
    elif opcion == 3:
        print(f'\n Dinero en la cuenta: ${saldo} ')
    elif opcion == 4:
        print(f'\n Gracias por utilizar su cajero automatico, hasta pronto')
        break
    else:
        print(f'\n Error, opcion en el menu no existene')
        print()