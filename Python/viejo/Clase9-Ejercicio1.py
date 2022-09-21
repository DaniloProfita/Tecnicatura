#Ingresar por consola si es un año bisiesto o no
#Repetir hasta que el usuario lo desee
print('Comprobamos que anio es bisiesto')
opcion = 1
while opcion == 1:
    num = int(input("Ingrese un anio: "))
    if (num % 4 == 0) and (num % 100 != 0) or (num % 400 == 0):
        print('El año es bisiesto')
        opcion = int(input("Para seguir adelante digite el numero 1: "))
    else:
        print('El año NO es bisiesto')
        opcion = int(input("Para seguir adelante digite el numero 1: "))