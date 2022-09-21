#Ejercicio10: No repetir caracteres
#Hacer un programa que pida una cadena por teclado
#Luego meter los caracteres en una lista sin repetir

cadena = input("Ingrese un caracter: ")
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print(f'\n Lista de caracteres sin repetir ninguno: \n {lista} ')