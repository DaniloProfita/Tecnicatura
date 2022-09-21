#Ejercicio 5: Factorial de un numero positivo
#Hacer un programa para calcular el factorial de un numero positivo


factorial = 1
numero = int(input('Digite un numero positivo'))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo'))


for i in range(1, numero+1):
    factorial *= i

print(f'\n El factorial de {numero} es: {factorial} ')