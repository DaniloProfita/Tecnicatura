#Ejercicio 4: Sumar número pares dentro de un rango
#Hacer un programa para sumar números pares dentro de un rango, por ejemplo:
#Suma de números pares del 2 al 30 => suma = 240

num1 = int(input("Ingrese el primer numero del rango: "))
num2 = int(input("Ingrese el segundo numro del rango: "))
suma = 0
for i in range(num1, num2+1):
    if i % 2 == 0:
        suma += i


print(f"La suma de numeros pares dentro del rango es: {suma}")