#Ingresar N enteros, visualizar la suma de los numero pares de la lista.
#Cuantos numeros pares existen y cual es el promedio de los numero impares.
n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))
i = 1
suma_pares = 0
cont_pares = 0
suma_impares = 0
cont_impares = 0

for i in range (n_elementos):
    i += 1
    print("Digite  el  ",i,"°  numero:  ")
    num = int(input())
    if (num % 2 == 0):
        suma_pares = suma_pares + num
        cont_pares += 1
    else: 
        suma_impares = suma_impares + num
        cont_impares += 1

if (cont_pares == 0):
    print("No se han digitado numeros pares")
else: 
    print("La suma de los numeros pares es: ", suma_pares)
    print("El conteo de los numero pares es: ", cont_pares)

if (cont_impares == 0):
    print("No se han digitado numeros impares")
else: 
    prom_impares = suma_impares / cont_impares
    print("El promedio de impares es: ", prom_impares)