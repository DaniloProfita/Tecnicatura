#Ejercicio 7: Juego adivina el numero
#Realizar un juego para adivinar un numero
#Para ello se debe generar un numero aleatorio entre 1 - 100, luego ir pidiendo numero indicando  "es mayor" o "es menor"
#El proceso termina cuando el usuario acierta y alli se debe mostrar el numero de intentos
import random
aleatorio = random.randint(0, 100)
contador = 0

while not False:
    numero = int(input("\n Ingrese un numero: "))
    contador += 1
    if numero == aleatorio:
        print(f'\n El numero {numero} es correcto!, el numero de intentos fue {contador}')
        break;
    elif numero > aleatorio:
        print(f'\n Es menor a {numero} ')
    elif numero < aleatorio:
        print(f'\n Es mayor a {numero} ')