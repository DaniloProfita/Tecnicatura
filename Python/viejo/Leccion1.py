'''
miVaribale = 3
print(miVaribale)
miVaribale = "Hola Mundo"
print(miVaribale)
miVaribale = 3.5
print(miVaribale)
x = 10
y = 2
z = x + y
print(id(x))
print(id(y))
print(id(z))

#Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))#Con esto muestra el tipo de dato que es la variable
x = 14.5
print(x)
print(type(x))
x = "Hola Mundo"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

#Manejo de cadenas (String)
miGrupoFavorito = "Duko"
caracteristicas = "Usa autotune"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

#Tipos Booleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Procesar la entrada del usuario
#Funcion input
#resultado = input("Digite un numero") #Regresa un dato tipo string
#print(resultado)

#Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("El resultado de la suma: ", suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")

division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
"""
alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
print("El area del rectangulo es: ", area)
perimetro = (alto + ancho) * 2
print("El perimetro del rectangulo es: ", perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)

#Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable - 2
miVariable3 -= 2
print(miVariable3)

#miVariable3 = miVariable * 3
miVariable3 *= 3
print(miVariable3)

#miVariable3 = miVariable / 2
miVariable3 /= 2
print(miVariable3)
"""
"""
#Operadores de Comparacion
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

#Operador Mayor que
resultado = d > b
print(resultado)

#Operador Menor que
resultado = d < b
print(resultado)

#Operador Mayor o igual que
resultado = d >= b
print(resultado)

#Operador Menor o igual que
resultado = d <= b
print(resultado)
"""
"""
num = int(input("Ingrese un numero: "))
if num%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
"""
"""
edad = int(input("Ingrese una edad: "))
if edad >= 18:
    print(f"Es mayor de edad, {edad}")
else:
    print(f"Es menor de edad, {edad}")
"""
"""
#Operadores logicos
#Operador and
a = True
b = True
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

#Operador not
#Al ser un operador unario necesita unicamente un valor
resultado = not a
print(resultado)
"""
"""
numero = int(input("Ingrese un numero: "))
if numero >= 0 and numero <= 5:
    print(f'El numero {numero} ,se encuentra en el rango de 0 a 5')
else:
    print(f'El numero {numero} ,no esta en el rango entre el 0 y 5')
"""
"""
vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')
"""
"""
edad = int(input("Ingrese una edad: "))
if edad >= 20 and edad <= 30:
    print(f'La edad {edad} ,se encuentra en el rango entre 20 y 30 años')
else:
    print(f'La edad {edad} ,NO se encuentra en el rango entre 20 y 30 años')
"""
"""
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
if numero1 > numero2:
    print(f'El numero {numero1} es mayor que el numero {numero2}')
else:
    print(f'El numero {numero2} es mayor que el numero {numero1}')
"""

#Ejercicio: Tienda de libros
print('Digite los siguientes datos del libro')
nombre = input("Ingrese el nombre del libro: ")
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))
envioGratuito = input('Indicar si el envio es gratuito(True/False): ')
if envioGratuito == 'True':
    envioGratuito == True
elif envioGratuito == 'False':
    envioGratuito == False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envio Gratuito?: {envioGratuito}
''')