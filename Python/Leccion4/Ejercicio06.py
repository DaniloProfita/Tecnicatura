#Ejercicio 6: Tabla de multiplicar
#Hacer un programa que pida un  numero por teclado y guarde
#en una lista su tabla de multiplicar hasta el 10, Ej:
#Si digita el 5 la lista tendra: 5-10-15-20-25-30-35-40-45-50

lista = []
numero = int(input("Ingrese un numero: "))

for i in numero:
    if i < 10:
        lista.append(lista)
else:
    print('Se acabaron los elementos de la tabla')

print(lista)