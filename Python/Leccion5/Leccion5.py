#Comenzamos con Funciones
#Definimos una funcion
import numbers
from unittest import result

'''
def MiFuncion():
    print('Saludos desde funcion')

MiFuncion()
MiFuncion()

#Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person =["Ariel", "Bentacud"]
show(person[0], person[1])
show(*person)
person2 =["Dano", "Profita"]
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print('Esto se termino')

#List comprehension, lista de compresion
names = ["Papo", "Dano", "Lau", "Pepe"]
alongP = [p for p in names if p[0] == 'P']#Regresa una nueva lista
print(alongP)

bottleC = [
    {"name": "Quilmes", "country": "Arg"},
    {"name": "Corona", "country": "Mx"},
    {"name": "Stella Artois", "country": "Belgium"},
]
Arg = [b for b in bottleC if b["country"] == 'Arg']
print(Arg)
print(bottleC)


#Paso de Argumentos (funciones)
def MiFuncion2(name, lastName):
    print('Saludos')
    print(f'Nombre: {name}, Apellido: {lastName}')
MiFuncion2('Dano', 'Profita')
MiFuncion2('Ariel', 'Bentacud')
MiFuncion2('Jorge', 'Pedrosa')
'''
'''

#La palabra return en funciones
#Creamos una funcion para suma
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(78, 22)}')

def sumar2(a = 1, b = 3):
    return a + b
resultado = sumar2()
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar2(22, 22)}')


#Argumentos, variables en funciones
#se usa cuando no sabemos la cantidad de nombres que vamos a pasar
def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listaNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela')
'''
'''

def listarTerminos(**terminos):#Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')
listarTerminos()#Nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviorment', PK='Primary Key')
listarTerminos(ElDiez='Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombre2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombre2)
desplegarNombres('Carla')
# desplegarNombres(10) No se puede iterar
desplegarNombres({10, 11})#Ahora si se puede iterar porque es una tupla
desplegarNombres([10, 11])#Tambie se puede porque lo convertimos a lista


#Funciones Recursivas
def factorial(numero):
    if numero == 1:#Caso base
        return 1
    else:
        return numero * factorial(numero-1)#Caso recursivo
resultado = factorial(5)
print(f'El factorial del numero 5 es: {resultado}')
'''


#Que el usuario ingrese el numero para calcular el facorial
num = int(input("Ingrese un numero:: "))
def factorialTarea(num):
    if num == 1:
        return 1
    else:
        return num * factorialTarea(num-1)
resultado = factorialTarea(num)
print(f'El factorial del numero {num} es: {resultado}')